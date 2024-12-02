import os
from jose import ExpiredSignatureError, JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

class JWTService:
    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        if expires_delta is None:
            expires_delta = timedelta(minutes=60)
        expire = datetime.utcnow() + expires_delta
        to_encode = data.copy()
        to_encode.update({"exp": expire, "sub": data["sub"]})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except ExpiredSignatureError:
            return None  # Ou lançar uma exceção personalizada
        except JWTError:
            return None
