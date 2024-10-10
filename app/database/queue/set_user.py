from app.database.models.user import User
from app.database.models.async_session import async_session

from app.database.queue.check_user import check_user


async def set_user(telegram_id: int):
    user_exists = await check_user(telegram_id)

    if not user_exists:
        async with async_session() as session:
            async with session.begin():
                new_user = User(telegram_id=telegram_id)
                session.add(new_user)
    else:
        print(f"User with telegram_id {telegram_id} already exists.")