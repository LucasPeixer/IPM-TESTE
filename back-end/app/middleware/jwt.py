from fastapi import HTTPException, Header
from app.services.token_service import JWTService

# Instância do serviço JWT
jwt_service = JWTService()
#Confere 
def verify_jwt_token(Authorization: str = Header(...)):
    try:

        if not Authorization.startswith("Bearer "):
            raise HTTPException(status_code=400, detail="Invalid token format")

        token = Authorization[7:]

        payload = jwt_service.decode_token(token)

        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload["sub"]

    except Exception as e:
        raise HTTPException(status_code=401, detail="Unauthorized")
