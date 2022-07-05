# открываем файл и читаем
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# итерируем по строкам 
def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]

# делаем шаг строк согласно количеству индигриентов
def split_ingredients_data(lst):
    return lst[:1] + [i.split(' | ') for i in lst[2:]]

# структурируем данные согласно задания
def lst_to_dict(lst):
    return {lst[0]: 
    [{'ingredient_name': i[0], 'quantity': int(i[1]), 'measure': i[2]} for i in lst[1:]]
    }

# создаём словарь, вносим в него параметры 
def data_loads(file_path):
    cook_book = {}
    text = read_file(file_path)
    dish_list = split_text(text)
    format_dish_list = [split_ingredients_data(i) for i in dish_list]
    for i in format_dish_list:
        cook_book.update(lst_to_dict(i))
    return cook_book
 
res = data_loads('Home_work\DZ №7\dish_list.txt')
 
cook_book = print(res)

# функция ввода количества персон
def person_count():
    county = int(input('Введите количество человек: '))
    return county

#функция ввода блюд
def dishes(cook_book):
    menu = cook_book.keys()
    menu_show = ', '.join(menu)
    print(f'Наше меню:\n{menu_show}')
    while True:
        dish_list = input('Введите блюда через запятую (напр. \"Омлет, Фахитос\"): ').split(', ')
        for item in dish_list:
            if item in menu_show:
                return dish_list
            else:
                print('Вы ввели неправильно либо несуществующие блюда, повторите попытку снова!')
            
ready_dishes = dishes(res)
ready_count = person_count()

# функция вызова требуемых индигриентов
def get_shop_list_by_dishes(dishes, person_count):
    for item in dishes:
        item = res.get(item)
        for i in item:
            from_key = i.get('ingredient_name')
            from_how = {'quantity': int(i.get('quantity')*person_count), 'measure': i.get('measure')}
            print(from_key, from_how)

get_shop_list_by_dishes(ready_dishes, ready_count)