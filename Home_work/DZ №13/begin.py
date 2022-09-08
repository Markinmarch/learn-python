import psycopg2
import enter_data

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_data(
                        name VARCHAR(40) NOT NULL,
                        last_name VARCHAR(40) NOT NULL,
                        num_phone VARCHAR UNIQUE NULL,
                        email VARCHAR UNIQUE NULL                       
                    );
                    """)
        conn.commit()

        cur.execute("""
                    INSERT INTO user_data (name, last_name, num_phone, email)
                    VALUES (%s, %s, %s, %s)
                    RETURNING name, last_name;
                    """, (enter_data.add_data.name,
                          enter_data.add_data.last_name,
                          enter_data.add_data.phone,
                          enter_data.add_data.mail))
        print(cur.fetchone())
    
        # cur.execute("""
        #             UPDATE user_data SET num_phone=%s
        #             WHERE name=%s AND last_name=%s;
        #             """,('1234567890', 'Марк', 'Изотов'))
        # cur.execute("""
        # SELECT * FROM user_data;
        # """)
        # print(cur.fetchall())
    
conn.close()

                    # """, ({enter_data.add_data.name},
                    #       {enter_data.add_data.last_name},
                    #       {enter_data.add_data.phone},
                    #       {enter_data.add_data.mail}))