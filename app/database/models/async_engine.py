import os

from dotenv import load_dotenv, find_dotenv

from sqlalchemy.ext.asyncio import create_async_engine


load_dotenv(find_dotenv())

database_url = os.getenv('DATABASE_ASYNC_URL')

if not database_url:
    raise ValueError("DATABASE_ASYNC_URL is not set in the environment variables.")

async_engine = create_async_engine(database_url, echo=True)