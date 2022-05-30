print('Программа для повара')
person = int(input('Введите количество персон: '))
#   Долбанный список пордуктов!
cook_book = [
  ['Салат:',
      [
        ['картофель:', 100, 'гр.'],
        ['морковь:', 50, 'гр.'],
        ['огурцы:', 50, 'гр.'],
        ['горошек:', 30, 'гр.'],
        ['майонез:', 70, 'мл.'],
      ]
  ],
  ['Пицца:',  
      [
        ['сыр:', 50, 'гр.'],
        ['томаты:', 50, 'гр.'],
        ['тесто:', 100, 'гр.'],
        ['бекон:', 30, 'гр.'],
        ['колбаса:', 30, 'гр.'],
        ['грибы:', 20, 'гр.'],
      ],
  ],
  ['Фруктовый десерт:',
      [
        ['хурма:', 60, 'гр.'],
        ['киви:', 60, 'гр.'],
        ['творог:', 60, 'гр.'],
        ['сахар:', 10, 'гр.'],
        ['мед:', 50, 'мл.'],  
      ]
  ]
]
#   Распаковываем из списков списки, из списков списки, из...
for dish, ingrs in cook_book:
  print()
  print(f'{dish.capitalize()}:')
  for name, q, measure in ingrs:
    print(f'{name.capitalize()}, {q*person} {measure}')
