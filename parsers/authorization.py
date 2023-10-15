# External libreries
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from starlette.requests import Request

# Own libraries
from python.jwt_manager import decode_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = decode_token(auth.credentials)
        print(data)
        if data is None:
            HTTPException(status_code=403, detail='Credenciales no válidas')
