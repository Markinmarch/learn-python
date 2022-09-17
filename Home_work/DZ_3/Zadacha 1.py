print('Программа для знакомств')
#   Вводим имена, присваивая имя переменной и сразу же делим через split, тем самым создавая список
boys = input('Введите имя парней через запятую и затем "Enter" для завершения ввода: ').split(',')
#   Тут всё то же самое, только с девочками
girls= input('Введите имя девушек через запятую и затем "Enter" для завершения ввода: ').split(',')

#   Это я закоментил списки по ДЗ
# boys_name = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls_name = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Количество парней и девушек разняться, кто-то останется без пары!')
else:
    print('Идеальные пары: ')
    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(f'{boy} и {girl}')
