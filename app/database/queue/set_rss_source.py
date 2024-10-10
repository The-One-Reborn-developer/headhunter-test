from app.database.models.async_session import async_session
from app.database.models.rss_sources import RSSSources


async def set_rss_source(url: str, user_id: int):
    async with async_session() as session:
        async with session.begin():
            new_rss_source = RSSSources(url=url, user_id=user_id)
            
            session.add(new_rss_source)