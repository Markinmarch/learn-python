# pip install beautifulsoup4
# pip install lxml/ pip install html.parser
import requests
from bs4 import BeautifulSoup
import csv

KEYWORDS = ['джун', 'IT', 'веб', 'python']

url = 'https://tproger.ru/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

# формируем расширенный поисковой список
# из представленных ключевых слов
def preparing_search_list(keywords):

    search_list = []
    for item_words in keywords:
        replacing_list = item_words.title()
        search_list.append(replacing_list)
    get_new_list = search_list + keywords
    return get_new_list


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

# функция запроса ссылок для возвращения даты
def date_return():
    
    date_list = []
    for item in desired_list():
        url = item.split(' --- ')[1]
        resp = requests.get(url).text
        soup = BeautifulSoup(resp, 'html.parser')
        get_teg = soup.find_all('time')
        for item_teg in get_teg:
            date_list.append(item_teg['title'])
    return date_list

# формируем готовый список по ТЗ
def ready_pars_list():
    text_list = []
    for item_text in desired_list():
        pars_text = (item_text.split(' --- ')[1])
        text_list.append(pars_text)
    link_list = []
    for item_link in desired_list():
        pars_link = (item_link.split(' --- ')[0])
        link_list.append(pars_link)
    time_list = []
    for item_time in date_return():
        time_list.append(item_time)
    pars_list = []
    for txt, lnk, tm in zip(text_list, link_list, time_list):
        pars_str = f'{tm} - {lnk} - {txt}'
        pars_list.append(pars_str)
    sort_pars_list = sorted(pars_list, key = lambda x: x[0:2])
    return sort_pars_list

# сохраняем всё в отдельный файл
def create_files():

    with open(r'DZ_17_web_scraping/work_files/file.csv', 'w', encoding = 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(
                [['time', 'header', 'link']]
            )
        
    for item_pars in ready_pars_list():
        elements_for_table = item_pars.split(' - ')
        with open(r'DZ_17_web_scraping/work_files/file.csv', 'a', encoding = 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                [elements_for_table[0], elements_for_table[1], elements_for_table[2]]
            )