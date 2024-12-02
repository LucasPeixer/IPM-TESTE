from app.services.password_service import PasswordService
from app.services.token_service import JWTService
from app.repository.user_repository import UserRepository
from app.schemas.user_schema import UserCreate
from datetime import timedelta
from typing import Optional
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Buscar as variáveis SECRET_KEY e ALGORITHM
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class UserUseCase:
    def __init__(self, user_repository: UserRepository, password_service: PasswordService, token_service: JWTService):
        self.user_repository = user_repository
        self.password_service = password_service
        self.token_service = token_service

    def create_user(self, user_data: UserCreate):
        password_hash = self.password_service.hash_password(user_data.password)

        user_data_dict = user_data.dict(exclude={"password"})
        user_data_dict['password_hash'] = password_hash

        return self.user_repository.create_user(user_data_dict)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        return self.token_service.create_access_token(data, expires_delta)