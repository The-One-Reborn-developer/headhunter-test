from sqlalchemy import select

from app.database.models.rss_sources import RSSSources
from app.database.models.async_engine import async_engine


async def check_rss_source(url: str) -> bool:
    async with async_engine.connect() as conn:
        result = await conn.execute(select(RSSSources).where(RSSSources.url == url))
        rss_source = result.scalar_one_or_none()

        return rss_source is not None