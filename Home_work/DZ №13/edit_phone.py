import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
        def update_data():
            
            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
            name = name_last_name[0]
            last_name = name_last_name[1]
            new_num_phone = input('Введите новый номер телефона: ')
            cur.execute("""
                        UPDATE user_data SET num_phone=%s
                        WHERE name=%s AND last_name=%s;
                        """,(new_num_phone, name, last_name))
            cur.execute("""
            SELECT * FROM user_data
            WHERE name = %s AND last_name = %s;
            """, (name, last_name))
            return cur.fetchone()
        
        print(update_data())
    
conn.close()

class edit_data():
    
    while True:
        
        what_data_to_enter = input(
            'Введите номер предложенных вариантов для редакции:\n'
            '1. Имя\n'
            '2. Фамилию\n'
            '3. Номер телефона\n'
            '4. Адрес электронной почты\n'
            'Нажимите Enter, если хотите прекратить операцию: '
            )
    
        if what_data_to_enter == '':
            print('Завершено!')
            break
        
        elif what_data_to_enter == '1':
            find_by = input('Введите фамилию, номер телефона или адрес почты: ')
            break
        
        elif what_data_to_enter == '2':
            find_by = input('Введите имя, номер телефона или адрес почты: ')
            break
        
        elif what_data_to_enter == '3':
            find_by = input('Введите имя, фимилию или адрес почты: ')
            break
        
        elif what_data_to_enter == '4':
            find_by = input('Введите имя, номер телефона или адрес почты: ')
            break
        
        else:
            print('Вы ввели неверные данные, повторите попытку!')
        