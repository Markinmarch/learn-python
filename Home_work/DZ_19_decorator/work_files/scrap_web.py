import requests
from bs4 import BeautifulSoup
from work_files import decorator, param_decor

# @decorator.log_info
# def web_scrap(url):
    
#     response = requests.get(url).text
#     soup = BeautifulSoup(response, 'html.parser')
    
#     lst_href = []
#     search_by_a = soup.find_all('a')
#     for search_by_href in search_by_a:
#         item_text = search_by_href.text.strip()
#         item_url = search_by_href.get('href')
#         ready_to_lst = f'{item_text}: {item_url}'
#         lst_href.append(ready_to_lst)
#     return lst_href

@param_decor.param_decor_with_path('DZ_19_decorator/logs/csv_log.csv')
def web_sscrap(url):
    
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