import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()


ENGINE = create_engine(os.getenv("DATABASE"))
SESSION = sessionmaker(bind=ENGINE)
session = SESSION()
BASE = declarative_base()


def create_db():
    BASE.metadata.create_all(bind=ENGINE)