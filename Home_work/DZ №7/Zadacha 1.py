# открываем файл и читаем
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# приводим в читабельный вид 
def split_text(text):
    return [i.splitlines() for i in text.split('\n\n')]

# выводим отдельно индигриенты
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
 
print(res)