import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
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