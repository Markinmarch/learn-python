# открываем, читаем файл
def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')
        
file_show = open_file('Home_work\DZ №7\dish_list.txt')

# структурируем данные в требуемый вид с учётом задания
def structure_data(file_name):
    r = file_name[0].split('\n')
    # print(r[2:])
    for i in r[2:]:
        l = []
        x = i.split(' | ')
        l.append(i)
        print(x)



    

structure_data(file_show)