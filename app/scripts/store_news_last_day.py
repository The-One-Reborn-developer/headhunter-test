import json

from app.scripts.get_news_last_day import get_news_last_day
from app.database.queue.get_all_rss_sources import get_all_rss_sources


async def store_news_last_day():
    try:
        sources = await get_all_rss_sources()

        news_data = []

        for source in sources:
            news = await get_news_last_day(source.url)
            user_id = source.user_id

            news_data.append({
                'user_id': user_id,
                'news': news
            })

            with open('app/temp/last_day.json', 'w', encoding='utf-8') as f:
                json.dump(news_data, f, ensure_ascii=False, indent=4)
                    
    except Exception as e:
        print(f'Error: {e}')