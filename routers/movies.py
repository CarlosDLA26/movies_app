# External libraries
import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi import Path
from fastapi import Query
from fastapi import status
from sqlalchemy import func
from sqlalchemy import select
from typing import List

# Own libraries
from db import Session
from models.models import MovieDB
from parsers.movie import MovieCreate
from python.metadata.tags import Tags


movies_router = APIRouter(
    prefix='/movies',
    tags=[Tags.MOVIE.value]
)


@movies_router.get(
    '/random',
    status_code=status.HTTP_200_OK)
def get_random_movies() -> List[MovieCreate]:

    """Obtiene 10 películas aleatorias de la base de datos
    """

    session = Session()
    stmt = select(MovieDB).order_by(func.random()).limit(10)
    res = session.execute(stmt)
    response = [movie[0].get_response_model() for movie in res]
    return response


# @movies_router.get(
#     '/{id_movie}',
#     response_model=Movie,
#     status_code=status.HTTP_200_OK)
# def get_movie(id_movie: str):
#     if id_movie in data_movies.keys():
#         return data_movies[id_movie]
#     else:
#         return JSONResponse(
#             content='No se ha encontrado la película',
#             status_code=status.HTTP_404_NOT_FOUND)


# @movies_router.get(
#     '/',
#     response_model=dict[str, Movie],
#     status_code=status.HTTP_200_OK)
# def get_movies_by_category(
#         category: str = Query(default='Acción', min_length=1, max_length=50)):
#     movies_data = {
#         id_movie: movie for id_movie, movie in data_movies.items()
#         if movie['category'] == category}
#     return movies_data


# @movies_router.post(
#     '/post',
#     response_model=dict[str, Movie],
#     status_code=status.HTTP_201_CREATED)
# def post_new_movie(new_movie: Movie):
#     new_id = str(uuid.uuid4())
#     movies = {**data_movies, new_id: new_movie.model_dump()}
#     return movies


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
