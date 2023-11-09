# External libraries
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Own libraries
from config import get_settings


env = get_settings(getenv('ENV'))

engine = create_engine(
    env.SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False})
Session = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
