# External libraries
from datetime import date
from pydantic import BaseModel
from pydantic import Field


class MovieBase(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    adult: bool = Field(default=False)
    budget: int = Field(ge=0)
    original_language: str = Field(min_length=1, max_length=150)
    overview: str = Field(min_length=10, max_length=1200)
    year: int = Field(ge=0, le=date.today().year)
    vote_average: float = Field(ge=0.0, le=10.0)
    vote_count: int = Field(gt=0)
    runtime: int = Field(gt=0)
    production_countries: str = Field(min_length=1, max_length=50)
    genres: list


class MovieCreate(MovieBase):
    # TODO: Agregar clase config de ejemplo
    id: int


class Movie(MovieBase):
    # TODO: Agregar clase config de ejemplo
    pass
