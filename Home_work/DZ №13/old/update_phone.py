import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
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
    
conn.close()