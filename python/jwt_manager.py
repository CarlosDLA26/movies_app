# External libraries
from jwt import decode
from jwt import encode


def create_token(data: dict) -> str:
    token = encode(payload=data, key='secreto', algorithm='HS256')
    return token


def decode_token(token: str) -> dict:
    data = decode(token, key='secreto', algorithms=['HS256'])
    return data
