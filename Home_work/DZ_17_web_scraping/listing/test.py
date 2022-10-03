# pip install beautifulsoup4
# pip install lxml/ pip install html.parser
import requests
from bs4 import BeautifulSoup

KEYWORDS = ['джун', 'IT', 'веб', 'python']



# def preparing_search_list(keywords):

#     search_list = []
#     for item_words in keywords:
#         replacing_list = item_words.title()
#         search_list.append(replacing_list)
#         get_new_list = search_list + keywords
#     return(get_new_list)

# def desired_list():
    
#     link_list = []
#     for words in preparing_search_list(KEYWORDS):
#         search_by_words = soup.find_all('div', class_= 'article__container-text')
#         for item_find in search_by_words:
#             text_p = item_find.find('p').text.strip()
#             text_a = item_find.find('a').text
#             link_a = item_find.find('a')['href']
#             ready_blocks = f'{text_a} --- {link_a} --- {text_p}'.strip()
#             if words in ready_blocks:
#                 link_list.append(ready_blocks)
#     return list(set(link_list))

# print(desired_list())

# with open(r'DZ_17_web_scraping/html/habr.html', 'w', encoding = 'utf-8') as file:
#     file.write(response)
# print(response)


# =====================================================================================
# def preparing_search_list(keywords):

#     search_list = []
#     for item_words in keywords:
#         replacing_letters = item_words.replace(f'{item_words[0]}', f'[{item_words[0].swapcase() + item_words[0]}]')
#         search_list.append(replacing_letters)
#     return(search_list)

# ready_words = preparing_search_list(KEYWORDS)
# ===========================================================================================

def preparing_search_list(keywords):

    search_list = []
    for item_words in keywords:
        replacing_list = item_words.title()
        search_list.append(replacing_list)
        get_new_list = search_list + keywords
    return(get_new_list)


# with open(r'DZ_17_web_scraping/html/habr.html', 'w', encoding = 'utf-8') as file:
#     file.write(response)
# print(response)

# def desired_list():
#     link_list = []
#     for words in ready_words:
#         search_by_words = soup.find_all('a', class_= 'article__link', text = re.compile(f"({words})"))
#         # print(search_by_words)
#         for one_by_one in search_by_words:
#             find_text = one_by_one.text.strip()
#             find_link = one_by_one['href']
#             ready_block = f'{find_text} --- {find_link}'
#             link_list.append(ready_block)
#     return list(set(link_list))

# print(desired_list())

# ====================================================================================
# функция вызова ссылок с текстом по ключевым словам
# получил требуемые значения по общему классу
def desired_list():
    
    url = 'https://tproger.ru/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
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
    print(sort_pars_list)
 
    
# ready_pars_list()