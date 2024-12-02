from pydantic import BaseModel, EmailStr
from app.validators.user_validator import UserValidators


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    # Usando os validadores definidos na classe UserValidators
    _validate_name = UserValidators.validate_name
    _validate_email = UserValidators.validate_email
    _validate_password = UserValidators.validate_password

    class Config:
        orm_mode = True
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


class Login(BaseModel):
    email: EmailStr
    password: str

    # Usando o validador para o email e password no Login
    _validate_email = UserValidators.validate_email
    _validate_password = UserValidators.validate_password

    class Config:
        from_attributes = True
