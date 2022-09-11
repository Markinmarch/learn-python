import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
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

conn.close()