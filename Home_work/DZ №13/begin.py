import psycopg2
import enter_data

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS user_data(
                        id SERIAL PRIMARY KEY NOT NULL,
                        name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(40) NOT NULL,
                        num_phone VARCHAR UNIQUE NULL,
                        email VARCHAR UNIQUE NULL                       
                    );
                    ''')
        conn.commit()
    
        cur.execute(f"""
                    INSERT INTO user_data(id, name, last_name, num_phone, email)
                    VALUES(
                    '{enter_data.name}',
                    '{enter_data.last_name}',
                    '{enter_data.phone}',
                    '{enter_data.mail}')
                    RETURNING id, name, last_name;
                    """)
        print(cur.fetchone()) 
    
conn.close()

                        # {enter_data.enter_data().get('name')},
                        # {enter_data.enter_data().get('last_name')},
                        # {enter_data.enter_data().get('mail')},
                        # {enter_data.enter_data().get('num_phone')}