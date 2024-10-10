import redis
import json

from app.scripts.get_news_last_hour import get_news_last_hour
from app.database.queue.get_all_rss_sources import get_all_rss_sources


async def store_news_last_hour():
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    try:
        sources = await get_all_rss_sources()

        for source in sources:
            news = await get_news_last_hour(source.url)
            r.set(f'news_last_hour_{source.user_id}', json.dumps(news))
            print(f'Success: Stored news for user {source.user_id} in Redis.\n{news}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        r.close()