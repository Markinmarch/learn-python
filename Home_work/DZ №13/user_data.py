# создаём ячейку данных о пользователе

def enter_data():
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    mail = input('Введите адреса электронной почты через запятую: ').split(',')
    phone = input('Введите номера телефонов через запятую: ').split(',')
    data_dict = {
        'name': name,
        'last_name': last_name,
        'mail': mail,
        'num_phone': phone
            }
    return data_dict
   
# print(enter_data())