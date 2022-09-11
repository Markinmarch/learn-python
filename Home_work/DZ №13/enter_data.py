import psycopg2

with psycopg2.connect(database = 'HW_13', user = 'postgres', password = 'M4rk130t08') as conn:
    with conn.cursor() as cur:
        
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

conn.close()