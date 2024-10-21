from sqlalchemy import select

from database.models.task import Task
from database.models.sync_session import sync_session


def put_task(id, title, description):
    with sync_session() as session:
        with session.begin():
            task = session.execute(select(Task).filter_by(id=id)).scalar()

            if task:
                task.title = title
                task.description = description
            else:
                raise ValueError(f'Task with id {id} is not found')