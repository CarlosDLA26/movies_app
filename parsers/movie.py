# External libraries
from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    overview: str
    year: int
    rating: float
    category: str
