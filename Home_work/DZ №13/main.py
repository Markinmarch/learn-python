import psycopg2

name_DB = input('Введите имя базы данных: ')#'HW_13'
user_name = input('Введите имя пользователя базы данных: ')#'postgres'
user_pass = input('Введите пароль от базы данных: ')#''

with psycopg2.connect(database = name_DB, user = user_name, password = user_pass) as conn:
    with conn.cursor() as cur:
        
        print('Создание таблицы.')        
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_data(
                        name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(40) NOT NULL,
                        num_phone VARCHAR UNIQUE NULL,
                        email VARCHAR UNIQUE NULL                       
                    );
                    """)
        conn.commit()
        print('Таблица создана!')
        
        while True:
        
            how_do_you_whant = input('Введите номер варианта параметра: \n'
                                    '1. Добавить нового клиента\n'
                                    '2. Добавить телефон для клиента\n'
                                    '3. Изменить данные о клиенте\n'
                                    '4. Удалить телефон клиента\n'
                                    '5. Удалить клиента\n'
                                    '6. Найти клиента по его данным\n'
                                    'Нажмите Enter для завершения операции\n')
            
            if how_do_you_whant == '1':
                
                def enter_data_user():
                
                    name = input('Введите имя: ')
                    last_name = input('Введите фамилию: ')
                    mail = input('Введите адреса электронной почты через запятую: ')
                    phone = input('Введите номера телефонов через запятую: ')
                    cur.execute("""
                                INSERT INTO user_data (name, last_name, num_phone, email)
                                VALUES (%s, %s, %s, %s)
                                RETURNING name, last_name;
                                """, (name,
                                    last_name,
                                    phone,
                                    mail
                                    ))
                    return cur.fetchall()
                        
                print(enter_data_user())
                
            elif how_do_you_whant == '2':
                
                def add_phone():
                
                    print('Добавляем телефон пользователю.')
                    name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                    name = name_last_name[0]
                    last_name = name_last_name[1]
                    new_num_phone = input('Введите новый номер телефона: ')
                    cur.execute("""
                                SELECT num_phone FROM user_data
                                WHERE name=%s AND last_name=%s;
                                """, (name, last_name))
                    for old_num_phone in cur.fetchone():
                        ready_num_phone = old_num_phone, new_num_phone
                        cur.execute("""
                                    UPDATE user_data
                                    SET num_phone = %s
                                    WHERE name=%s AND last_name=%s;
                                    """, (ready_num_phone ,name, last_name))
                    cur.execute("""
                    SELECT * FROM user_data
                    WHERE name = %s AND last_name = %s;
                                """, (name, last_name))
                    return cur.fetchall()
                
                print(add_phone())
                
            elif how_do_you_whant == '3':
                
                while True:
                    
                    what_data_to_edit = input(
                        'Введите номер предложенных вариантов для редакции:\n'
                        '1. Имя\n'
                        '2. Фамилию\n'
                        '3. Номер телефона\n'
                        '4. Адрес электронной почты\n'
                        'Нажимите Enter, если хотите прекратить операцию: '
                        )
                
                    if what_data_to_edit == '':
                        print('Завершено!')
                        break
                    
                    elif what_data_to_edit == '1':
                        
                        def edit_data():
                            
                            print('Поиск пользователя')
                            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                            name = name_last_name[0]
                            last_name = name_last_name[1]
                            new_name = input('Введите новое имя: ')
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))
                            cur.execute("""
                                        UPDATE user_data
                                        SET name = %s
                                        WHERE name = %s AND last_name = %s;
                                        """,(new_name, name, last_name))
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (new_name, last_name))        
                            return cur.fetchall()
                        
                        print(edit_data())
                        print('Готово!')
                        break
                    
                    elif what_data_to_edit == '2':
                        
                        def edit_data():
                            
                            print('Поиск пользователя')
                            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                            name = name_last_name[0]
                            last_name = name_last_name[1]
                            new_last_name = input('Введите новую фамилию: ')
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))
                            cur.execute("""
                                        UPDATE user_data
                                        SET name = %s
                                        WHERE name = %s AND last_name = %s;
                                        """,(new_last_name, name, last_name))
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, new_last_name))        
                            return cur.fetchall()
                        
                        print(edit_data())
                        print('Готово!')
                        break
                    
                    elif what_data_to_edit == '3':
                        
                        def edit_data():
                            
                            print('Поиск пользователя')
                            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                            name = name_last_name[0]
                            last_name = name_last_name[1]
                            new_num_phone = input('Введите новый номер телефона: ')
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))
                            cur.execute("""
                                        UPDATE user_data
                                        SET name = %s
                                        WHERE name = %s AND last_name = %s;
                                        """,(new_num_phone, name, last_name))
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))        
                            return cur.fetchall()
                        
                        print(edit_data())
                        print('Готово!')
                        break
                    
                    elif what_data_to_edit == '4':
                        
                        def edit_data():
                            
                            print('Поиск пользователя')
                            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                            name = name_last_name[0]
                            last_name = name_last_name[1]
                            new_email = input('Введите новый адрес эл.почты: ')
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))
                            cur.execute("""
                                        UPDATE user_data
                                        SET name = %s
                                        WHERE name = %s AND last_name = %s;
                                        """,(new_email, name, last_name))
                            cur.execute("""
                                        SELECT * FROM user_data
                                        WHERE name = %s AND last_name = %s;
                                        """, (name, last_name))        
                            return cur.fetchall()
                        
                        print(edit_data())
                        print('Готово!')
                        break
                    
                    else:
                        print('Вы ввели неверные данные, повторите попытку!')
                
            elif how_do_you_whant == '4':
                
                def delete_phone():
                
                    print('Удаление телефона пользователя.')
                    name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                    name = name_last_name[0]
                    last_name = name_last_name[1]
                    cur.execute("""
                                UPDATE user_data SET num_phone=%s
                                WHERE name=%s AND last_name=%s;
                                """,('', name, last_name))
                    cur.execute("""
                    SELECT * FROM user_data
                    WHERE name = %s AND last_name = %s;
                    """, (name, last_name))
                    print(f'Телефон пользователя {name} {last_name} удалён!')
                    return cur.fetchone()
                
                print(delete_phone())
            
            elif how_do_you_whant == '5':
                
                def delete_user():
                    
                    print('Удаление пользователя.')
                    name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
                    name = name_last_name[0]
                    last_name = name_last_name[1]
                    cur.execute("""
                                DELETE FROM user_data
                                WHERE name=%s AND last_name=%s;
                                """,(name, last_name))
                    cur.execute("""
                    SELECT * FROM user_data;
                    """)
                    print(f'Пользователь под именем {name} {last_name} удалён!')
                    for item in cur.fetchall():
                        print(item)
            
                delete_user()
                
            elif how_do_you_whant == '6':
                
                def search_data():
                
                    print('Поиск пользователя')
                    find_by = input('Введите данные пользователя: ')
                    cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s OR last_name = %s OR num_phone = %s OR email = %s;
                        """, (find_by, find_by, find_by, find_by))
                    return cur.fetchall()

                print(search_data())

            elif how_do_you_whant == '':
                print('Операция завершена!')
                break
            
            else:
                print('Некорректные данные, повторите попытку!')
            
conn.close()