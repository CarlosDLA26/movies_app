# External libreries
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy import String

# Own libraries
from db import Base


class MovieDB(Base):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    adult = Column(Boolean, default=False)
    budget = Column(Integer)
    original_language = Column(String(150))
    overview = Column(String(1200))
    vote_average = Column(Float(2))
    vote_count = Column(Integer)
    runtime = Column(Integer)
    production_countries = Column(String(50))

    genres = relationship('MovieGenreDB', back_populates='movie')


class GenreDB(Base):

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    type_gen = Column(String(30))

    movies = relationship('MovieGenreDB', 'genre')


class MovieGenreDB(Base):

    __tablename__ = 'movies_genres'

    movie_id = Column(Integer, ForeignKey('movies.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    movie = relationship('MovieDB', back_populates='genres')
    genre = relationship('GenreDB', back_populates='movies')
