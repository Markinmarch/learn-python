import create
import enter_data
def get_start():

    # name_DB = input('Введите имя базы данных: ')
    # user_name = input('Введите имя пользователя базы данных: ')
    # user_pass = input('Введите пароль от базы данных: ')
    
    
    # while True:
    how_do_you_whant = input('Введите номер варианта параметра: \n'
                            '1. Добавить нового клиента\n'
                            '2. Добавить телефон для клиента\n'
                            '3. Изменить данные о клиенте\n'
                            '4. Удалить телефон клиента\n'
                            '5. Удалить клиента\n'
                            '6. Найти клиента по его данным\n'
                            'Нажмите Enter для завершения операции\n')
        
    if how_do_you_whant == 1:
        print(enter_data.enter_data_user())
            
get_start()