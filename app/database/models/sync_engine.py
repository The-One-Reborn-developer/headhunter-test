import os

from sqlalchemy import create_engine

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

database_url = os.getenv('DATABASE_URL')

print(f"Loaded DATABASE_URL: {database_url}")

sync_engine = create_engine(database_url, echo=True)