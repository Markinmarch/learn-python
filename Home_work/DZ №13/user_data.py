# создаём ячейку данных о пользователе

def enter_data():
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    while True:
        mail = input('Введите адреса электронной почты через запятую: ').split(',')
        if mail == False:
            print('Адрес почты отсутсвует')
        else:
            break
        phone = input('Введите номера телефонов через запятую: ').split(',')
        if phone == False:
            print('Номер телефона отсутствует')
        if mail and phone == False:
            print('Мы не можем внести Ваши данные без каких-либо контактов с вами.\n'
                  'Попробуйте ввести данные снова!')
            break
    data_dict = {
        'name': name,
        'last_name': last_name,
        'mail': mail,
        'num_phone': phone
            }
    return data_dict
   
print(enter_data())