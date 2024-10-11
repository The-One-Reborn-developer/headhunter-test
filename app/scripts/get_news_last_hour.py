import pytz
import feedparser
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

def fetch_rss_feed(url):
    return feedparser.parse(url)

def get_news_last_hour(url, hours=1):
    feed = fetch_rss_feed(url)

    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(tz)

    recent_news = []
    for entry in feed.entries:
        try:
            published_str = entry.published

            if 'GMT' in published_str:
                published_str = published_str.replace('GMT', '+0000')

            published_formats = [
                '%a, %d %b %Y %H:%M:%S %z',
                '%Y-%m-%dT%H:%M:%S.%fZ',
                '%Y-%m-%dT%H:%M:%SZ',
                '%d.%m.%Y'
            ]

            published = None
            for fmt in published_formats:
                try:
                    published = datetime.strptime(published_str, fmt)
                    break
                except ValueError:
                    continue

            if published is None:
                print(f"Could not parse date for entry: {entry.title} - raw date string: {published_str}")
                published = None

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
