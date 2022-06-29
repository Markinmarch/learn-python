# открываем, читаем файл
import enum

def open_file(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')
        
file_show = open_file('Home_work\DZ №7\dish_list.txt')

# cоздаём переменную num для перебирания блюд
# def dish_rate(ready_file):
#     numb = range(len(ready_file)) 
#     for number in numb:
#         x = number
#         print(x)

# num = dish_rate(file_show)

num = 0
# структурируем данные в требуемый вид с учётом задания
# создание value
def structure_data_value(ready_file, num):
    value_name = ready_file[num].split('\n')
    for item in value_name[2:]:
        indigrients = item.split(' | ')
        lst = []
        dict_dish = {'ingredient_name': indigrients[0], 'quantity': indigrients[1], 'measure': indigrients[2]}
        lst.append(dict_dish)
        print(lst)
    #     key_name = ready_file[num].split('\n')
    #     cook_book = {key_name[0]:[dict_dish for i in indigrients]}
    # cook_book.update()
    # print(cook_book)

        # print(key_name[0])
        # print(dict_dish)

# структурируем данные в требуемый вид с учётом задания
# создание key
def structure_data_key(ready_file, num):
    key_name = ready_file[num].split('\n')
    print(key_name[0])


# structure_data_key(file_show, num)
structure_data_value(file_show, num)

# cook_book = {w : q}
# cook_book.update()
# print(cook_book)

# def huef(i):
#     def qwert(x):
#         return x + i
#     return qwert
# new = huef(100)
# print(new(200))


