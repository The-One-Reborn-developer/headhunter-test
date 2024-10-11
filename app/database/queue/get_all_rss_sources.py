from sqlalchemy import select

from app.database.models.session import session
from app.database.models.rss_sources import RSSSources


def get_all_rss_sources():
    new_session = session()
    try:
        rss_sources = new_session.execute(select(RSSSources)).scalars().all()  # Perform synchronous query
        return rss_sources
    finally:
        new_session.close()