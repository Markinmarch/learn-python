documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Питонов"},
        {"type": "invoice", "number": "11-2", "name": "Иерофан Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Эдуард Шевелюров"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_people_name(name):
  what_number_doc = input('Введите номер документа: ')
  for people in name:
    if what_number_doc == people['number']:
      return(people['name'])
# print(get_people_name(documents))

def get_shelf_number(shelf_number):
  what_number_doc = input('Введите номер документа: ')
  for shelf_value in shelf_number:
    if what_number_doc in shelf_number.get(shelf_value):
      return(f'Документ находится на полке № {shelf_value[0]}')
  return('Отсутствуют документы с данным номером!')
# print(get_shelf_number(directories))

def get_list(docs):
  for doc in docs:
    return (f"{doc['type']} {doc['number']} {doc['name']}")
print(get_list(documents))

def add_doc(docs_add):
  shelf = input('Введите номер полки куда положить документ. ')
  if shelf not in docs_add:
      return 'Нет такой полки'
  doc = {}
  for info in ('type', 'number', 'name'):
      doc[info] = input(f'{info}: ')
  docs_add[shelf] = docs_add.get(shelf).append(doc['number'])
  return 'Документ добавлен'

# while True:
#   print('Возможные команды: p, s, l, a')
#   comand = input('Введите название команды ')
 
#   if comand == 'p':
#     print(get_people_name(documents))
    
#   elif comand == 's':
#     print(get_shelf_number(directories))
    
#   elif comand == 'l':
#     print(get_list(documents))
    
#   elif comand == 'a':
#     print(add_doc(directories))
# print(documents[::])