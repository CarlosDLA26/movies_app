# External libraries
from pydantic import BaseModel
from pydantic import Field


class GenreBase(BaseModel):
    type_gen: str = Field(min_length=1, max_length=30)

    movies: list


class GenreCreate(GenreBase):
    # TODO: Agregar clase config de ejemplo
    id: int


class Genre(GenreBase):
    # TODO: Agregar clase config de ejemplo
    pass
