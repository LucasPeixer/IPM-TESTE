from fastapi import APIRouter, Depends
from app.controller.user_controller import UserController
from app.usecase.user_usecase import UserUseCase
from app.repository.user_repository import UserRepository
from app.services.password_service import PasswordService
from app.services.token_service import JWTService
from app.db.db import get_db
from app.schemas.user_schema import UserCreate, UserResponse, Login
from sqlalchemy.orm import Session

# Funções de dependência para cada serviço e repositório
def get_password_service():
    return PasswordService()

def get_token_service():
    return JWTService()

def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)

def get_user_usecase(user_repository: UserRepository = Depends(get_user_repository),
                     password_service: PasswordService = Depends(get_password_service),
                     token_service: JWTService = Depends(get_token_service)):
    return UserUseCase(user_repository, password_service, token_service)

def get_user_controller(user_usecase: UserUseCase = Depends(get_user_usecase),
                         password_service: PasswordService = Depends(get_password_service)):
    return UserController(user_usecase, password_service)

# Criando as rotas
def create_user_routes(router: APIRouter):
    @router.post("/register", response_model=UserResponse)
    def register_user(user_data: UserCreate, user_controller: UserController = Depends(get_user_controller)):
        return user_controller.create_user(user_data)

    @router.post("/login")
    def login_user(login_data: Login, user_controller: UserController = Depends(get_user_controller)):
        return user_controller.login(login_data)
