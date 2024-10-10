from sqlalchemy import select

from app.database.models.rss_sources import RSSSources
from app.database.models.engine import engine


async def check_rss_source(url: str) -> bool:
    async with engine.connect() as conn:
        result = await conn.execute(select(RSSSources).where(RSSSources.url == url))
        rss_source = result.scalar_one_or_none()

        return rss_source is not None