import requests
import feedparser

async def check_url(url: str) -> bool:
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code} for URL: {url}")
            return False
        else:
            print(f"Success: Received status code {response.status_code} for URL: {url}")

        feed = feedparser.parse(response.content)

        if feed.bozo:
            print(f"Error: Invalid RSS feed for URL: {url}")
            return False
        else:
            print(f"Success: Valid RSS feed for URL: {url}")

        return True

    except requests.exceptions.RequestException as e:
        print(f"Error: {e} for URL: {url}")
        return False
