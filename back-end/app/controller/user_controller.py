from fastapi import HTTPException
from app.usecase.user_usecase import UserUseCase
from app.schemas.user_schema import UserCreate, UserResponse, Login
from app.services.password_service import PasswordService

class UserController:
    def __init__(self, user_usecase: UserUseCase, password_service: PasswordService):
        self.user_usecase = user_usecase
        self.password_service = password_service

    def create_user(self, user_data: UserCreate):
        user = self.user_usecase.create_user(user_data)
        return UserResponse(**user.__dict__)

    def login(self, login_data: Login):
        user = self.user_usecase.get_user_by_email(login_data.email)
        if not user or not self.password_service.verify_password(login_data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        access_token = self.user_usecase.create_access_token(data={"sub": user.email})
        return {"access_token": access_token, "token_type": "bearer"}
