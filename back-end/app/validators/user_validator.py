from pydantic import validator, EmailStr
from typing import Optional
import re

class UserValidators:
    @staticmethod
    @validator('email')
    #Valida se o email tem o formato correto.
    def validate_email(cls, v: EmailStr):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, v):
            raise ValueError("Email inválido. Por favor, forneça um email válido.")
        return v
    
    @staticmethod
    @validator('password')
    #Valida se a senha tem pelo menos 8 caracteres e inclui um número e uma letra
    def validate_password(cls, v: str):
        if len(v) < 8:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isdigit() for char in v):
            raise ValueError("A senha deve conter pelo menos um número.")
        if not any(char.isalpha() for char in v):
            raise ValueError("A senha deve conter pelo menos uma letra.")
        return v

    @staticmethod
    @validator('name')
    #Valida se o nome não é vazio e tem pelo menos 3 caracteres.
    def validate_name(cls, v: str):
        if len(v.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        return v
