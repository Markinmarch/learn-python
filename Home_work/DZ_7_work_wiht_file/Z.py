# открываем, читаем файл
def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')
        
file_show = open_file('Home_work\DZ №7\dish_list.txt')
# структурируем данные в требуемый вид с учётом задания
def structure_data(dish_list):
    for item in dish_list:
        res = item.split('\n')
        for i in res[2:]:
            ras = i.split(' | ')
            cook_book = {res[0]:[{'ingredient_name': ras[0]}, {'quantity': ras[1]}, {'measure': ras[2]}]}
            print(cook_book.get(res[0]))
structure_data(file_show)