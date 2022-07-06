# открываем файл и читаем
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# открываем файл и читаем
def write_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.write()

file = read_file('Home_work\DZ №7\text\1.txt')