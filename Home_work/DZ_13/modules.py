import psycopg2
import getpass

# метод для входа в БД
class input_data_DB():
    
    name_DB = input('Введите имя базы данных: ')#'HW_13'
    user_name = input('Введите имя пользователя базы данных: ')#'postgres'
    user_pass = getpass.getpass('Введите пароль от базы данных: ')#''

# функция создания таблицы БВ
def get_create_table():

    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
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
            print('Таблица создана!')
            conn.commit()
            conn.close()
    
# функция добавляет нового пользователя  
def add_user():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
                
            name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            mail = input('Введите адреса электронной почты через запятую: ')
            phone = input('Введите номера телефонов через запятую: ')
            cur.execute("""
                        INSERT INTO user_data (name, last_name, num_phone, email)
                        VALUES (%s, %s, %s, %s)
                        RETURNING name, last_name, num_phone, email;
                        """, (name,
                            last_name,
                            phone,
                            mail
                            ))
            print(f'Готово: {cur.fetchall()}')

# добавляем ещё один(!) телефон
def add_phone():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
            
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
            print(cur.fetchall())

# изменяем параметр name
def edit_name():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
            
            print('Поиск пользователя')
            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
            name = name_last_name[0]
            last_name = name_last_name[1]
            new_parametr = input('Введите новое имя: ')
            cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s AND last_name = %s;
                        """, (name, last_name))
            cur.execute("""
                        UPDATE user_data
                        SET name = %s
                        WHERE name = %s AND last_name = %s
                        RETURNING name, last_name;
                        """,(new_parametr, name, last_name))
            print('Готово!') 
            print(cur.fetchall())          

# изменяем параметр last_name
def edit_last_name():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
            
            print('Поиск пользователя')
            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
            name = name_last_name[0]
            last_name = name_last_name[1]
            new_parametr = input('Введите новую фамилию: ')
            cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s AND last_name = %s;
                        """, (name, last_name))
            cur.execute("""
                        UPDATE user_data
                        SET last_name = %s
                        WHERE name = %s AND last_name = %s
                        RETURNING name, last_name;
                        """,(new_parametr, name, last_name))
            print('Готово!') 
            print(cur.fetchall())
            
# изменяем параметр num_phone
def edit_phone():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
            
            print('Поиск пользователя')
            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
            name = name_last_name[0]
            last_name = name_last_name[1]
            new_parametr = input('Введите новый телефон: ')
            cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s AND last_name = %s;
                        """, (name, last_name))
            cur.execute("""
                        UPDATE user_data
                        SET num_phone = %s
                        WHERE name = %s AND last_name = %s
                        RETURNING name, last_name, num_phone;
                        """,(new_parametr, name, last_name))
            print('Готово!') 
            print(cur.fetchall())
            
# изменяем параметр num_phone
def edit_email():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
            
            print('Поиск пользователя')
            name_last_name = input('Введите имя и фамилию пользователя: ').split(' ')
            name = name_last_name[0]
            last_name = name_last_name[1]
            new_parametr = input('Введите новый адрес почты: ')
            cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s AND last_name = %s;
                        """, (name, last_name))
            cur.execute("""
                        UPDATE user_data
                        SET email = %s
                        WHERE name = %s AND last_name = %s
                        RETURNING name, last_name, email;
                        """,(new_parametr, name, last_name))
            print('Готово!') 
            print(cur.fetchall())            

# удаление телефона пользователя            
def delete_phone():
    
    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:

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
            print(cur.fetchone())
            
# удаление пользователя            
def delete_user():

    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:
                                
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

# поиск пользователя
def search_data():

    with psycopg2.connect(
        database = input_data_DB.name_DB,
        user = input_data_DB.user_name,
        password = input_data_DB.user_pass
        ) as conn:
        
        with conn.cursor() as cur:   
                         
            print('Поиск пользователя')
            find_by = input('Введите данные пользователя: ')
            cur.execute("""
                        SELECT * FROM user_data
                        WHERE name = %s OR last_name = %s OR num_phone = %s OR email = %s;
                        """, (find_by, find_by, find_by, find_by))
            print(cur.fetchall())
          
            
            
                        
            