# External libraries
from fastapi import APIRouter
from fastapi.responses import Response
from fastapi import status

# Own libraries
from db.db import data_movies
from metadata.tags import Tags


movies_router = APIRouter(
    prefix='/movies', 
    tags=[Tags.MOVIE.value]
)


@movies_router.get('/')
def get_movies():
    return data_movies


@movies_router.get('/{id_movie}')
def get_movie(id_movie: int):
    movie_data = list(filter(
        lambda x: x['id'] == id_movie, data_movies
    ))
    if movie_data:
        return movie_data[0]
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
