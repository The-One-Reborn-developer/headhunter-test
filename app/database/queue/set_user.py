from app.database.models.user import User
from app.database.models.async_session import async_session

async def set_user(user_id: int):
    async with async_session() as session:
        async with session.begin():
            new_user = User(telegram_id=user_id)
            
            session.add(new_user)