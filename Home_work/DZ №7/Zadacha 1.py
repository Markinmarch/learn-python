# открываем, читаем файл
def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')
        
file_show = open_file('Home_work\DZ №7\dish_list.txt')

# структурируем данные в требуемый вид с учётом задания
# создание value
def structure_data_value(file_name, dish):
    r = file_name[dish].split('\n')
    for i in r[2:]:
        x = i.split(' | ')
        d = {'ingredient_name': x[0], 'quantity': x[1], 'measure': x[2]}
        print(d)

# структурируем данные в требуемый вид с учётом задания
# создание key
# def structure_data_key(file_name):

# создать для dish функцию, которая будет по сути индексировать номера блюд!!!
    

structure_data_value(file_show)