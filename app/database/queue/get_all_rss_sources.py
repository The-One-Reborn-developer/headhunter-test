from sqlalchemy import select

from app.database.models.rss_sources import RSSSources
from app.database.models.async_session import async_session


async def get_all_rss_sources():
    async with async_session() as session:
        async with session.begin():
            rss_sources = await session.execute(select(RSSSources))

            return rss_sources.scalars().all()