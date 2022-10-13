import requests
from bs4 import BeautifulSoup
import csv
import datetime
from work_files import scrap_web
import inspect


def log_info(enter_func):
    
    with open(r'DZ_19_decorator/logs/csv_log.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(
            [['Дата', 'Время', 'Имя функции', 'Аргументы', 'Путь']]
        )
         
    def func_enter(*args, **kwargs):
        
        date_now = datetime.datetime.now().strftime('%d-%m-%Y')
        time_now = datetime.datetime.now().strftime('%H:%M:%S:%f')
        func_args = inspect.signature(enter_func)
        return [date_now, time_now, enter_func(*args, **kwargs), enter_func.__name__, inspect.getabsfile(enter_func), func_args]
    return func_enter
#         enter_func(*args, **kwargs)

    
        
#     # for item_pars in ready_pars_list():
#     #     elements_for_table = item_pars.split(' - ')
#     #     with open(r'DZ_17_web_scraping/work_files/file.csv', 'a', encoding = 'utf-8') as file:
#     #         writer = csv.writer(file)
#     #         writer.writerow(
#     #             [elements_for_table[0], elements_for_table[1], elements_for_table[2]]
#     #         )    

# date_today = datetime.datetime.today().strftime('%d-%m-%Y')
# print(date_today)

# time_now = datetime.datetime.now().strftime('%H:%M:%S:%f')
# print(time_now)

# def scrap_web(link):
    
    
# 'DZ_17_web_scraping/main.py'

@log_info
def web_scrap(url):
    
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    
    lst_href = []
    search_by_a = soup.find_all('a')
    for search_by_href in search_by_a:
        item_text = search_by_href.text.strip()
        item_url = search_by_href.get('href')
        ready_to_lst = f'{item_text}: {item_url}'
        lst_href.append(ready_to_lst)
    return lst_href

func_argg = input('Введите адрес сайта: ')
print(web_scrap(func_argg))
# https://www.ozon.ru/
# print(dir(web_scrap))
# print(inspect.signature(web_scrap))