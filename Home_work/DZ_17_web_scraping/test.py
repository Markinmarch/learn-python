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



def date_return():
    date_list = []
    for i in desired_list():
        url = i.split(' --- ')[1]
        q = requests.get(url).text
        soup = BeautifulSoup(q, 'html.parser')
        y = soup.find_all('time')
        for i in y:
            date_list.append(i['title'])
    return date_list
        
# print(date_return())
# print(desired_list())
        
            
        
def qwerty():
    lst0 = []
    for i in desired_list():
        j = (i.split(' --- ')[1])
        lst0.append(j)
    lst1 = []
    for i in desired_list():
        d = (i.split(' --- ')[0])
        lst1.append(d)
    # print(lst1)
    lst2 = []
    for q in date_return():
        lst2.append(q)
    # print(lst2)
    lst3 = []
    for q1, d1, j1 in zip(lst0, lst1, lst2):
        x = f'{j1} - {d1} - {q1}'
        # print(x)
        lst3.append(x)
    # print(lst3)
    z = sorted(lst3, key = lambda u: u[0:2])
    print(z)
 
    
qwerty()