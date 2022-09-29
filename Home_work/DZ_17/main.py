# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/all/'
response = requests.get(url).text
# print(response.text)

soup = BeautifulSoup(response, 'lxml')

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# page_h1 = soup.find('h1')
# print(page_h1.text)

page_all_h1 = soup.find_all('h1')
print(page_all_h1)

