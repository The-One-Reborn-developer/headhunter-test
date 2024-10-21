from database.models.base import Base
from database.models.task import Task
from database.models.sync_engine import sync_engine


def create_database_tables() -> None:
    with sync_engine.begin() as conn:
        Base.metadata.create_all(conn)