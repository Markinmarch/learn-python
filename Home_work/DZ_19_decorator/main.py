import csv

def log_info(enter_func):
    
    def func_enter(*args, **kwargs):
        
        enter_func(*args, **kwargs)
        return enter_func

    with open(r'DZ_19_decorator/logs/csv_log.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(
            [['Дата', 'Время', 'Имя функции', 'Аргументы']]
        )
        
    # for item_pars in ready_pars_list():
    #     elements_for_table = item_pars.split(' - ')
    #     with open(r'DZ_17_web_scraping/work_files/file.csv', 'a', encoding = 'utf-8') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(
    #             [elements_for_table[0], elements_for_table[1], elements_for_table[2]]
    #         )    
    return enter_func