# External libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Own libraries
from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True,
    connect_args={'check_same_thread': False})
session_db = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
