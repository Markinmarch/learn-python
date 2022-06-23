# открываем и читаем файл
def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
# file_show = open_file('DZ №7\dish_list.txt').strip()
# print(file_show)

# превращаем текст в список для дальнейшей работы
def split_file(split_text):
    big_dish_list = split_text.split('\n')
    print(big_dish_list)
# q = split_file(file_show)

# структура данных
def structure_data()