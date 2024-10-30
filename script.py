import requests
import json

from bs4 import BeautifulSoup


base_url = "https://quotes.toscrape.com/page/{}/"
total_pages = 10

quotes_data = []

for page in range(1, total_pages + 1):
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        
        author = quote.find('small', class_='author').get_text()
        
        tags = [tag.get_text() for tag in quote.find('div', class_='tags').find_all('a', class_='tag')]

        quotes_data.append({
            'text': text,
            'author': author,
            'tags': tags
        })

with open('quotes.json', 'w') as f:
    json.dump(quotes_data, f, indent=4)