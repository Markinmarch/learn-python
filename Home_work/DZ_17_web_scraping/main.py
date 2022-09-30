# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'
response = requests.get(url).text
# with open(r'DZ_17_web_scraping/html/habr.html', 'w', encoding = 'utf-8') as file:
#     file.write(response)
# print(response)

soup = BeautifulSoup(response, 'html.parser')

find_all_keywords = soup.find('div', {'class': 'tm-articles-list', 'data-test-id': 'articles-list'}).find_all(text = re.compile(KEYWORDS))
print(find_all_keywords)
