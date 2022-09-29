# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'
response = requests.get(url).text
with open(r'DZ_17_web_scraping/html/habr.html', 'w', encoding = 'utf-8') as file:
    file.write(response)
# print(response)

soup = BeautifulSoup(response, 'lxml')

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# page_h1 = soup.find('h1')
# print(page_h1.text)

# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find('div', class_ = 'user')

# print(user_name)