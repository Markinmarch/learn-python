import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
        def search_data():
            
            print('Поиск пользователя')
            find_by = input('Введите данные пользователя: ')
            cur.execute("""
                SELECT * FROM user_data
                WHERE name = %s OR last_name = %s OR num_phone = %s OR email = %s;
                """, (find_by, find_by, find_by, find_by))
            return cur.fetchall()
        
        print(search_data())
          
conn.close()