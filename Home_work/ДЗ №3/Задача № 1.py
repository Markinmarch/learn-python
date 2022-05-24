print('Программа для знакомств')
#   Вводим имена, присваивая имя переменной и сразу же делим через split, тем самым создавая список
boys = input('Введите имя парней через запятую и затем "Enter" для завершения ввода: ').split(',')
#   Тут всё то же самое, только с девочками
girls= input('Введите имя девушек через запятую и затем "Enter" для завершения ввода: ').split(',')
# Сортируем списки ребят:
new_boys = sorted(boys, key=str.lower)
new_girls = sorted(girls, key=str.lower)

#   Это я закоментил списки по ДЗ
# boys_name = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls_name = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

for lovers in zip (new_boys, new_girls):
    if len(new_boys) == len(new_girls):
        print(f'Идеальные пары:\n{lovers[0]} и {lovers[1]}')
    else:
        print('Количество парней и девушек разняться, кто-то останется без пары!')