import psycopg2
import enter_data

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS user_data(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(40) NOT NULL,
                        num_phone VARCHAR(12) UNIQUE NULL,
                        email VARCHAR UNIQUE NULL                       
                    );
                    ''')
        conn.commit()
    
        cur.execute(f'''
                    INSERT INTO user_data(id, name, last_name, num_phone, e-mail)
                    VALUES (
                        1,
                        {enter_data.enter_data().get('name')},
                        {enter_data.enter_data().get('last_name')},
                        {enter_data.enter_data().get('num_phone')},
                        {enter_data.enter_data().get('mail')}
                        ) RETURNING id, name, last_name;
                    ''')
    print(cur.fetchone())

conn.close()