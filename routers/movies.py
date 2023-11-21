# External libraries
import uuid

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Path
from fastapi import status
from sqlalchemy import func
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
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
    return response


@movies_router.get(
    '/{id_movie}',
    status_code=status.HTTP_200_OK)
def get_movie(
        id_movie: str = Path(min_length=36, max_length=36)
    ) -> MovieCreate:

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
    session.execute(stmt)
    session.commit()
    # Se debe cerrar la sesión en la base de datos para evitar bloqueos
    session.close()
    return {**dict(new_movie), 'id': new_id}


@movies_router.put(
    '/put/{id_movie}',
    status_code=status.HTTP_200_OK)
def put_movie(
        new_data_movie: Movie,
        id_movie: str = Path(min_length=36, max_length=36)
    ) -> MovieCreate:

    """Actualiza datos de un registro en la base de datos
    """

    session = Session()
    stmt = select(MovieDB).where(MovieDB.id == id_movie)
    res = session.execute(stmt).all()
    if len(res) == 0:
        return JSONResponse(
            content='La película no se encuentra',
            status_code=status.HTTP_404_NOT_FOUND)
    stmt = update(MovieDB).where(MovieDB.id == id_movie).values(
        title=new_data_movie.title,
        adult=new_data_movie.adult,
        budget=new_data_movie.budget,
        original_language=new_data_movie.original_language,
        overview=new_data_movie.overview,
        release_date=new_data_movie.release_date,
        vote_average=new_data_movie.vote_average,
        vote_count=new_data_movie.vote_count,
        runtime=new_data_movie.runtime,
        production_countries=new_data_movie.production_countries
    )
    session.execute(stmt)
    session.commit()
    return res[0][0].get_response_model()


@movies_router.delete(
    '/delete/{id_movie}',
    status_code=status.HTTP_200_OK)
def delete_movie(id_movie: str) -> MovieCreate:

    """Borra datos de un registro en la base de datos
    """

    session = Session()
    stmt = select(MovieDB).where(MovieDB.id == id_movie)
    res = session.execute(stmt).all()
    if len(res) == 0:
        return JSONResponse(
            content='La película no se encuentra',
            status_code=status.HTTP_404_NOT_FOUND)
    # Se toman los datos antes de hacer commit para evitar un error al
    # buscar datos borrados
    data_movie = res[0][0].get_response_model()
    stmt = delete(MovieDB).where(MovieDB.id == id_movie)
    session.execute(stmt)
    session.commit()
    return data_movie
