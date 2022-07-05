file_name = 'Home_work/DZ №7/text'

def reading_file(file_name):
# получим объект файла
  with open(file_name, "r", encoding='utf-8') as file:
# итерация по строкам
    for line in file:
      print(line.strip())

def write_file(strint):
  with open('record', "w", encoding='utf-8') as file:
    file.write(strint)
    print('Файл записан')

def reading_file_2(file_name):
  with open(file_name, 'r', encoding='utf-8') as f:
    text = f.read().splitlines()
    print(text)
    print(len(text))
    str1 = ''.join(str(e) for e in text)
    print(str1)


reading_file_2(file_name)
