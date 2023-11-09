# External libreries
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

# Own libraries
from db import Base


class MovieDB(Base):

    __tablename__ = 'movies'

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    adult: Mapped[bool] = mapped_column(default=False, nullable=False)
    budget: Mapped[int] = mapped_column()
    original_language: Mapped[str] = mapped_column(String(150), nullable=False)
    overview: Mapped[str] = mapped_column(String(1200), nullable=False)
    release_date: Mapped[str] = mapped_column(String(10), nullable=False)
    vote_average: Mapped[float] = mapped_column(Float(2))
    vote_count: Mapped[int] = mapped_column()
    runtime: Mapped[int] = mapped_column(nullable=False)
    production_countries: Mapped[str] = mapped_column(String(50))

    genres = relationship('MovieGenreDB', back_populates='movie')

    def get_response_model(self) -> dict:
        res = {
            'id': self.id,
            'title': self.title,
            'adult': self.adult,
            'budget': self.budget,
            'original_language': self.original_language,
            'overview': self.overview,
            'release_date': self.release_date,
            'vote_average': self.vote_average,
            'vote_count': self.vote_count,
            'runtime': self.runtime,
            'production_countries': self.production_countries,
            'genres': [genre.genre_id for genre in self.genres]
        }
        return res


class GenreDB(Base):

    __tablename__ = 'genres'

    id: Mapped[str] = mapped_column(primary_key=True)
    type_gen: Mapped[str] = mapped_column(String(30), nullable=False)

    movies = relationship('MovieGenreDB', back_populates='genre')


class MovieGenreDB(Base):

    __tablename__ = 'movies_genres'

    id: Mapped[str] = mapped_column(primary_key=True)
    movie_id: Mapped[str] = mapped_column(ForeignKey('movies.id'), nullable=False)
    genre_id: Mapped[str] = mapped_column(ForeignKey('genres.id'), nullable=False)

    movie = relationship('MovieDB', back_populates='genres')
    genre = relationship('GenreDB', back_populates='movies')
