# ЗАДАЧА № 3
symbol = input('Введите любой символ: ')
print('Введите параметры квадрата:')
print('')
square_a = input('Введите сторону квадрата: ')
square_perimetr = int(square_a) * 4
print('Периметр треугольника будет равен ' , square_perimetr , '!')
square_area = int(square_a) ** 2
print('Площадь треугольника будет равна' , square_area , '!')
print('')
print('')
print('Введите параметры прямоугольника:')
print('')
rectangle_a = int(input('Введите размер стороны \'a\''))
rectangle_b = int(input('Введите размер стороны \'b\''))
rectangle_perimetr = ((rectangle_a) + (rectangle_b)) * 2
print('Периметр прямоугольника будет равен' , rectangle_perimetr , '!')
rectangle_area = (rectangle_a) * (rectangle_b)
print('Площадь прямоугольника будет равна' , rectangle_area , '!')
str = str(symbol) * int(square_perimetr + rectangle_area)
print('') 
print(str)
print('')
print('Приложение финансового планирования')
summa_zp = int(input('Введите сумму своей заработной платы: '))
ipoteka = int(input('Введите, сколько процентов уходит на ипотеку: '))
life = int(input('Введите, сколько процентов уходит на жизнь: '))
print('')
summa_ipoteka = (summa_zp * 12) / 100 * ipoteka
print('Сумма потраченная на ипотеку в этом году равна ' , summa_ipoteka , 'руб.')
summa_life = (summa_zp * 12) / 100 * life
print('Сумма потраченная на ипотеку в этом году равна ' , summa_life , 'руб.')        