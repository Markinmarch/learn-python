# открытие файла и чтение:
def open_cook_book():
    with open('DZ №7\dish_list.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(lines[0])
        # print(lines.index[0])
        # print(file.readline())
        # print(file.readline())
        # for line in file:
        #     print({line})
open_cook_book()