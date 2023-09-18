# External libraries
from fastapi import APIRouter

# Own libraries
from parsers.user import User
from python.jwt_manager import create_token
from python.metadata.tags import Tags


auth_router = APIRouter(
    prefix='/login', 
    tags=[Tags.AUTH.value]
)


@auth_router.post('')
def login(user: User):
    token = create_token(user.model_dump())
    return token
