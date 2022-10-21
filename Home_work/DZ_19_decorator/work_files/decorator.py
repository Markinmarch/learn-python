import csv
import datetime
import inspect
import os

def log_info(enter_func):
         
    def func_enter(*args, **kwargs):
        
        date_now = datetime.datetime.now().strftime('%d-%m-%Y')
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        main_func = enter_func(*args, **kwargs)
        main_lst = [date_now,
                    time_now,
                    enter_func.__name__,
                    main_func,
                    (args, kwargs),
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
            
        return func_enter
    
    
import csv
import datetime
import inspect

def param_decor_with_path(path):
    def log_info(enter_func):
        def func_enter(*args, **kwargs):
            date_now = datetime.datetime.now().strftime('%d-%m-%Y')
            time_now = datetime.datetime.now().strftime('%H:%M:%S')
            main_func = enter_func(*args, **kwargs)
            main_lst = [date_now,
                        time_now,
                        enter_func.__name__,
                        main_func,
                        (args, kwargs),
                        inspect.getabsfile(enter_func)]

            with open(path, 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(main_lst)
                
            return main_func
        return func_enter
    return log_info
