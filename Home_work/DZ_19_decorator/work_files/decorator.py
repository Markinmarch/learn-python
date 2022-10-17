import csv
import datetime
import inspect
import os

def log_info(enter_func):
         
    def func_enter(*args, **kwargs):
        
        date_now = datetime.datetime.now().strftime('%d-%m-%Y')
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        main_lst = [date_now,
                    time_now,
                    enter_func.__name__,
                    enter_func(*args, **kwargs),
                    inspect.getargspec(enter_func).args,
                    inspect.getabsfile(enter_func)]
        
        if os.path.isfile('DZ_19_decorator/logs/csv_log.csv'):
            pass
        else:
            with open(r'DZ_19_decorator/logs/csv_log.csv', 'w', encoding = 'utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(
                    [['Дата', 'Время', 'Имя функции', 'Информация', 'Аргументы', 'Путь']]
                )

        with open(r'DZ_19_decorator/logs/csv_log.csv', 'a', encoding = 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(main_lst)
            
        return main_lst
    return func_enter