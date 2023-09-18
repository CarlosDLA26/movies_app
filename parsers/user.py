# External libraries
from datetime import date
from pydantic import BaseModel
from pydantic import Field


class User(BaseModel):
    user: str
    password: str
