import requests
from bs4 import BeautifulSoup

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
    
# print(web_scrap('https://www.ozon.ru/'))
        
# if __name__ == '__main__':
    
#     web_scrap()