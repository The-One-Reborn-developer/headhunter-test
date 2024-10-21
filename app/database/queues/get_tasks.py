from sqlalchemy import select

from app.database.models.task import Task
from app.database.models.sync_session import sync_session


def get_tasks():
    with sync_session() as session:
        with session.begin():
            result = session.execute(select(Task))

            tasks = result.scalars().all()

            return tasks