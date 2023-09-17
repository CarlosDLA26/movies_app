# External libraries
from datetime import date
from pydantic import BaseModel
from pydantic import Field


class Movie(BaseModel):
    title: str = Field(min_length=1, max_length=50)
    overview: str = Field(min_length=10, max_length=100)
    year: int = Field(ge=0, le=date.today().year)
    rating: float = Field(ge=0, le=10.0)
    # TODO: Agregar un enum que tenga todos las posibles categorias de películas
    category: str = Field(min_length=1, max_length=50)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Título de ejemplo',
                'overview': 'Resumen de película',
                'year': 2017,
                'rating': 9.5,
                'category': 'Acción'
            }
        }
