# External libraries
import uuid

from fastapi import APIRouter
from fastapi.responses import Response
from fastapi import status

# Own libraries
from db.db import data_movies
from metadata.tags import Tags
from parsers.movie import Movie


movies_router = APIRouter(
    prefix='/movies', 
    tags=[Tags.MOVIE.value]
)


@movies_router.get('', response_model=dict[str, Movie])
def get_movies():
    return data_movies


@movies_router.get('/{id_movie}', response_model=Movie)
def get_movie(id_movie: str):
    if id_movie in data_movies.keys():
        return data_movies[id_movie]
    else:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@movies_router.get('/', response_model=dict[str, Movie])
def get_movies_by_category(category: str = 'Acción'):
    movies_data = {
        id_movie: movie for id_movie, movie in data_movies.items()
        if movie['category'] == category}
    return movies_data


@movies_router.post('/post', response_model=dict[str, Movie])
def post_new_movie(new_movie: Movie):
    new_id = str(uuid.uuid4())
    movies = {**data_movies, new_id: new_movie.model_dump()}
    return movies


@movies_router.put('/put/{id_movie}', response_model=dict[str, Movie])
def put_movie(id_movie: str, new_data_movie: Movie):
    if id_movie not in data_movies.keys():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    data_movies[id_movie] = new_data_movie.model_dump()
    return {id_movie: data_movies[id_movie]}


@movies_router.delete('/delete/{id_movie}', response_model=dict[str, Movie])
def delete_movie(id_movie: str):
    if id_movie not in data_movies.keys():
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    del data_movies[id_movie]
    return data_movies
