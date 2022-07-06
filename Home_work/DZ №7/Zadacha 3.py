catal_ad = 'Home_work/DZ №7/text/'

# функция открывает каталог с  файлами 
def mod_os(adress):
    import os
    file_list = os.listdir(adress)
    return file_list
file_list = mod_os(catal_ad)

# функция открывает файл
def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

# функция выводит список адрессов
def sluzhebka(lst, adress):
    where_is_the_file_from = [(adress + lst[i]) for i in range(0, len(lst))]
    return where_is_the_file_from
ready_to_adress_file = sluzhebka(file_list, catal_ad)
# print(ready_to_adress_file)

# функция выводит список количества строк
def how_many_lines(lst, adress):
    num_list_line = []
    how_many_lines = [open_file(adress + lst[i]) for i in range(0, len(lst))]
    for item in how_many_lines:
        item = len(item.split('\n'))
        num_list_line.append(str(item))
    return num_list_line
ready_to_lines = how_many_lines(file_list, catal_ad)
# print(ready_to_lines)

# функция компонует все элементы и сортирует по количеству строк
def sort_ready_text(lst, adress):
    read = [ready_to_adress_file[i] +'\n'+ ready_to_lines[i] +'\n'+ open_file(adress + lst[i]) for i in range(0, len(lst))]
    ready_text = sorted(read, key = len)
    return '\n'.join(ready_text)
read = sort_ready_text(file_list, catal_ad)
# print(read)

# функция записывает готовый файл
def write_file(ready_file):
    with open(r'Home_work/DZ №7/new_file.txt', 'w', encoding='utf-8') as file:
        return file.write(ready_file)
write_file(read)

