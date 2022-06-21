# открытие файла и чтение:
def open_cook_book():
    with open('ДЗ №7\dish_list.txt', 'r', encoding='utf-8') as file:
        cook_book = {file.read()}
        print(cook_book)
open_cook_book()