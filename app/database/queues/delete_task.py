from sqlalchemy import delete, select

from database.models.task import Task
from database.models.sync_session import sync_session


def delete_task(id):
    with sync_session() as session:
        with session.begin():
            task = session.execute(select(Task).filter_by(id=id)).scalar()

            if task:
                session.delete(task)
            else:
                raise ValueError(f'Task with id {id} is not found')