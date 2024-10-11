from sqlalchemy import select

from app.database.models.user import User
from app.database.models.async_engine import async_engine


async def check_user(telegram_id: int) -> bool:
    async with async_engine.connect() as conn:
        result = await conn.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalar_one_or_none()

        return user is not None