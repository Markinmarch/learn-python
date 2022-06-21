# открытие файла и чтение:
def open_cook_book():
    with open('ДЗ №7\dish_list.txt', 'r', encoding='utf-8') as file:
        dish_dict = {file.read()}
        print(dish_dict)
open_cook_book()