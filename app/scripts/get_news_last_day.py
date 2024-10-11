import pytz
import feedparser

from datetime import datetime, timedelta
from bs4 import BeautifulSoup


async def fetch_rss_feed(url):
    return feedparser.parse(url)

async def get_news_last_day(url, hours=24):
    feed = await fetch_rss_feed(url)

    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz)

    recent_news = []
    for entry in feed.entries:
        try:
            published_str = entry.published
            
            if 'GMT' in published_str:
                published_str = published_str.replace('GMT', '+0000')

            published = datetime.strptime(published_str, '%a, %d %b %Y %H:%M:%S %z')
        except (AttributeError, KeyError) as e:
            print(f"Error parsing date for entry: {entry} - {e}")
            published = None

        description = entry.summary
        description_stripped = BeautifulSoup(description, "html.parser").get_text() 

        if published and current_time - published <= timedelta(hours=hours):
            recent_news.append({
                'title': entry.title,
                'description': description_stripped,
                'link': entry.link,
                'author': entry.author if hasattr(entry, 'author') else 'Unknown',
                'published': published.strftime('%Y-%m-%d %H:%M:%S %Z')
            })
    
    return recent_news