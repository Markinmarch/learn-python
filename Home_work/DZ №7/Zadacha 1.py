from ctypes import Structure


def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()
# file_show = open_file('DZ №7\dish_list.txt')
# print(file_show)

# def split_file(split_text):