# Own libraries
from python.paths import Paths

SQLALCHEMY_DATABASE_URL = f'sqlite:///{str(Paths.database_movies)}'
