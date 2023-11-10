# External libraries
import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi import Path
from fastapi import Query
from fastapi import status
from sqlalchemy import func
from sqlalchemy import select, insert, update, delete
from typing import List

# Own libraries
from db import Session
from models.models import MovieDB
from parsers.movie import Movie
from parsers.movie import MovieCreate
from python.metadata.tags import Tags


movies_router = APIRouter(
    prefix='/movies',
    tags=[Tags.MOVIE.value]
)


@movies_router.get(
    '/random',
    status_code=status.HTTP_200_OK)
def get_random_movies(num: int = 10) -> List[MovieCreate]:

    """Obtiene películas aleatorias de la base de datos dependiendo del
    parámetro `num`.

    Args:
        num: número de películas aleatorias obtenidas por el endpoint.

    Returns:
        List[MovieCreate]: Películas obtenidas en la consulta::

            [
                {
                    'title': 'string',
                    'adult': false,
                    'budget': 0,
                    'original_language': 'string',
                    'overview': 'stringstri',
                    'release_date': 'stringstri',
                    'vote_average': 10,
                    'vote_count': 0,
                    'runtime': 0,
                    'production_countries': 'string',
                    'genres': [
                        'string'
                    ],
                    'id': 'string'
                }
            ]

    """

    session = Session()
    stmt = select(MovieDB).order_by(func.random()).limit(num)
    res = session.execute(stmt)
    response = [movie[0].get_response_model() for movie in res]
    print(response)
    return response


@movies_router.get(
    '/{id_movie}',
    status_code=status.HTTP_200_OK)
def get_movie(id_movie: str) -> MovieCreate:

    """Obtiene los datos de una película específica a partir de un id. En caso
    de no encontrar la película, devuelve una respuesta 404 o 400 en caso de
    que el id ingresado no corresponda a un uuid.

    Args:
        id_movie: id de la película que se desea obtener.

    Returns:
        MovieCreate: Datos de la película encontrada::

            {
                'title': 'string',
                'adult': false,
                'budget': 0,
                'original_language': 'string',
                'overview': 'stringstri',
                'release_date': 'stringstri',
                'vote_average': 10,
                'vote_count': 0,
                'runtime': 0,
                'production_countries': 'string',
                'genres': [
                    'string'
                ],
                'id': 'string'
            }

    """

    if len(id_movie) != 36:
        return JSONResponse(
            content='Verifique que el id de la ciudad tenga un formato de uuid',
            status_code=status.HTTP_400_BAD_REQUEST)

    session = Session()
    stmt = select(MovieDB).where(MovieDB.id == id_movie)
    res = session.execute(stmt).all()
    if len(res) == 1:
        return res[0][0].get_response_model()
    else:
        return JSONResponse(
            content='La película no fue encontrada',
            status_code=status.HTTP_404_NOT_FOUND)


@movies_router.post(
    '/post',
    status_code=status.HTTP_201_CREATED)
def post_movie(new_movie: Movie) -> MovieCreate:

    """Agrega una nueva película a la base de datos
    """

    session = Session()
    new_id = str(uuid.uuid4())
    stmt = insert(MovieDB).values(
        id=new_id,
        title=new_movie.title,
        adult=new_movie.adult,
        budget=new_movie.budget,
        original_language=new_movie.original_language,
        overview=new_movie.overview,
        release_date=new_movie.release_date,
        vote_average=new_movie.vote_average,
        vote_count=new_movie.vote_count,
        runtime=new_movie.runtime,
        production_countries=new_movie.production_countries
    )
    res = session.execute(stmt)
    session.commit()
    # Se debe cerrar la sesión en la base de datos para evitar bloqueos
    session.close()
    return {**dict(new_movie), 'id': new_id}


# @movies_router.put(
#     '/put/{id_movie}',
#     response_model=dict[str, Movie],
#     status_code=status.HTTP_200_OK)
# def put_movie(
#         new_data_movie: Movie,
#         id_movie: str = Path(min_length=36, max_length=36)):
#     if id_movie not in data_movies.keys():
#         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
#     data_movies[id_movie] = new_data_movie.model_dump()
#     return {id_movie: data_movies[id_movie]}


# @movies_router.delete(
#     '/delete/{id_movie}',
#     response_model=dict[str, Movie],
#     status_code=status.HTTP_200_OK)
# def delete_movie(id_movie: str):
#     if id_movie not in data_movies.keys():
#         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
#     del data_movies[id_movie]
#     return data_movies
