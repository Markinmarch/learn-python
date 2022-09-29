import modules

# функция создания таблицы БД
modules.get_create_table()

# функция добавляет нового пользователя             
modules.add_user()

# добавляем ещё один(!) телефон
modules.add_phone()
    
# изменяем параметр name
modules.edit_name()

# изменяем параметр last_name
modules.edit_last_name()
    
# изменяем параметр num_phone
modules.edit_phone()
    
# изменяем параметр email
modules.edit_email()
    
# удаление телефона пользователя            
modules.delete_phone()
    
# удаление пользователя            
modules.delete_user()
    
# поиск пользователя
modules.search_data()

# закрываем
modules.conn.close()
            
                        
            