from sqlalchemy import select

from app.database.models.task import Task
from app.database.models.sync_session import sync_session


def update_task(id, title, description):
    with sync_session() as session:
        with session.begin():
            task = session.execute(select(Task).filter_by(id=id)).scalar()
            task.title = title
            task.description = description