from sqlalchemy import select
from app.database.models.user import User
from app.database.models.engine import engine

async def check_user(telegram_id: int) -> bool:
    """
    Check if a user with the given telegram_id already exists in the database.

    :param telegram_id: The telegram ID of the user.
    :return: True if the user exists, False otherwise.
    """
    async with engine.connect() as conn:
        result = await conn.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar_one_or_none()

        return user is not None