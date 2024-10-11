import os

from sqlalchemy import create_engine

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database_url = os.getenv('DATABASE_SYNC_URL')

if not database_url:
    raise ValueError("DATABASE_SYNC_URL is not set in the environment variables.")

engine = create_engine(database_url, echo=True)