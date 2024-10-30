import requests

from bs4 import BeautifulSoup


base_url = "https://quotes.toscrape.com/page/{}/"
total_pages = 10

all_quotes = []
all_authors = []
all_tags = []

for page in range(1, total_pages + 1):
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        all_quotes.append(text)
        
        author = quote.find('small', class_='author').get_text()
        all_authors.append(author)
        
        tags = [tag.get_text() for tag in quote.find('div', class_='tags').find_all('a', class_='tag')]
        all_tags.append(tags)

with open('quotes.txt', 'w') as file:
    for i in range(len(all_quotes)):
        file.write(f"Quote: {all_quotes[i]}\n")
        file.write(f"Author: {all_authors[i]}\n")
        file.write(f"Tags: {', '.join(all_tags[i])}\n\n")
        file.write("-"*40 + "\n\n")