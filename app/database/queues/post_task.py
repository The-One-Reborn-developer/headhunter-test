from app.database.models.task import Task
from app.database.models.sync_session import sync_session


def post_task(title, description) -> None:
    with sync_session() as session:
        with session.begin():
            task = Task(title=title, description=description)

            session.add(task)