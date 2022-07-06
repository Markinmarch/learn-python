# открываем и читайем файлы
import os

def read_file(file_path):
    for file_name in os.listdir(file_path):
        with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as file:
            print(len(file.read().strip().split('\n')))

# записываем в новый файл
def write_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        return file.write('new')

adress_file = read_file('Home_work/DZ №7/text')

read_file(adress_file)

# считаем количество строк и сравниваем их
def how_lines(file_path):
    return len(file_path.strip().split('\n'))

# print(how_lines(adress_file))


