# ЗАДАЧА №1
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