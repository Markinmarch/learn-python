from work_files import scrap_web

if __name__ == '__main__':

    url = input('Введите адрес сайта: ')
    scrap_web.web_scrap(url)
    print('DZ_19_decorator/logs/csv_log.csv')
# https://www.ozon.ru/
# print(dir(web_scrap))
# print(inspect.signature(web_scrap))