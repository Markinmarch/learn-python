# pip install beautifulsoup4
# pip install lxml/ pip install html.parser
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['джун', 'IT', 'веб', 'python']

url = 'https://tproger.ru/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

def preparing_search_list(keywords):

    search_list = []
    for item_words in keywords:
        replacing_list = item_words.title()
        search_list.append(replacing_list)
        get_new_list = search_list + keywords
    return(get_new_list)

# функция вызова ссылок с текстом по ключевым словам
# получил требуемые значения по общему классу
def desired_list():
    
    link_list = []
    for words in preparing_search_list(KEYWORDS):
        search_by_words = soup.find_all('div', class_= 'article__container-text')
        for item_find in search_by_words:
            text_p = item_find.find('p').text.strip()
            text_a = item_find.find('a').text
            link_a = item_find.find('a')['href']
            ready_blocks = f'{text_a} --- {link_a} --- {text_p}'.strip()
            if words in ready_blocks:
                link_list.append(ready_blocks)
    return list(set(link_list))

print(desired_list())

# with open(r'DZ_17_web_scraping/html/habr.html', 'w', encoding = 'utf-8') as file:
#     file.write(response)
# print(response)

