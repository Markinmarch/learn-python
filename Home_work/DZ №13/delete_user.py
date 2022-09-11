import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
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

conn.close()