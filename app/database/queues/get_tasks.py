from sqlalchemy import select

from database.models.task import Task
from database.models.sync_session import sync_session


def get_tasks():
    with sync_session() as session:
        with session.begin():
            result = session.execute(select(Task))

            tasks = result.scalars().all()

            return [{'id': task.id, 'title': task.title, 'description': task.description, 'created_at': task.created_at} for task in tasks]