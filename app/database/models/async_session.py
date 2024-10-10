from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.database.models.engine import engine


async_session = async_sessionmaker(engine, expire_on_commit=False)