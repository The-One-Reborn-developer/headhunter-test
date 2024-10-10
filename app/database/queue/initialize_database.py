from app.database.models.base import Base
from app.database.models.user import User
from app.database.models.rss_sources import RSSSources
from app.database.models.engine import engine


async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)