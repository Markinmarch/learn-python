import csv
import datetime
import inspect

def param_decor_with_path(path):
    
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

            with open(path, 'a', encoding = 'utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(main_lst)
                
            return main_lst
        return func_enter
    return log_info

@param_decor_with_path('DZ_19_decorator/logs/csv_log.csv')
def div(a,b):
    return a+b

print(div(5, 10))