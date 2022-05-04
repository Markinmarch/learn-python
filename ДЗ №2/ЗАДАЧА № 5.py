month = str(input('Введите месяц рождения, например \'Март\':'))
date = int(input("Введите день рождения:"))
while month != ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']:
   print('Вы ввели неверные данные!')
   month = str(input('Введите месяц рождения, например \'Март\':'))
   if (date >= 11 and date <= 31 and month == 'Март') or (month == 'Апрель' and date >= 1 and date <= 10):
      print("Знак зодиака:Овен")   
   elif (date >= 11 and date <= 30 and month == 'Апрель') or (month == 'Май' and date >= 1 and date <= 10):
      print("Знак зодиака:Телец")
   elif (date >= 11 and date <= 31 and month == 'Май') or (month == 'Июнь' and date >= 1 and date <= 10):
      print("Знак зодиака:Близнецы")
   elif (date >= 11 and date <= 30 and month == 'Июнь') or (month == 'Июль' and date >= 1 and date <= 10):
      print("Знак зодиака:Рак")
   elif (date >= 11 and date <= 31 and month == 'Июль') or (month == 'Август' and date >= 1 and date <= 10):
      print("Знак зодиака:Лев")
   elif (date >= 11 and date <= 31 and month == 'Август') or (month == 'Сентябрь' and date >= 1 and date <= 10):
      print("Знак зодиака:Дева")
   elif (date >= 11 and date <= 30 and month == 'Сентябрь') or (month == 'Остябрь' and date >= 1 and date <= 10):
      print("Знак зодиака:Весы")
   elif (date >= 11 and date <= 31 and month == 'Октябрь') or (month == 'Ноябрь' and date >= 1 and date <= 10):
      print("Знак зодиака:Скорпион")
   elif (date >= 11 and date <= 30 and month == 'Ноябрь') or (month == 'Декабрь' and date >= 1 and date <= 10):
      print("Знак зодиака:Стрелец")
   elif (date >= 11 and date <= 31 and month == 'Декабрь') or (month == 'Январь' and date >= 1 and date <= 10):
      print("Знак зодиака:Козерог")
   elif (date >= 11 and date <= 31 and month == 'Январь') or(month == 'Февраль' and date >= 1 and date <= 10):
      print("Знак зодиака:Водолей")
   elif (date >= 11 and date <= 29 and month == 'Февраль') or(month == 'Март' and date >= 1 and date <= 10):
      print("Знак зодиака:Рыбы")
      break
