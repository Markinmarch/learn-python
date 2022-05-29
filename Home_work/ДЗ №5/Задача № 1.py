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
    print(f"{doc['type']} {doc['number']} {doc['name']}")
# (get_list(documents))

def add_doc(docs_add):
  shelf = input('Введите номер полки, куда положить документ. ')
  if shelf not in docs_add:
      return 'Нет такой полки'
  doc = {}
  for info in ('type', 'number', 'name'):
      doc[info] = input(f'{info}: ')
  docs_add[shelf] = docs_add.get(shelf).append(doc['number'])
  return 'Документ добавлен'
# print(add_doc(directories))

def del_doc(del_number, del_shelf):
  del_num = input('Введите номер документа: ')
  for doc in del_number:
    if del_num in doc['number']:
      doc['number'] = 'Удален'
  for directory_value in del_shelf.values():
    if del_num in directory_value:
      directory_value.remove(del_shelf)
      return('\n  Номер документа удален из каталога и полки!')
  return('\n  Внимание! Такого документа - нет.')
# print(del_doc(documents, directories))

while True:
  print('Возможные команды: p, s, l, a')
  comand = input('Введите название команды ')
 
  if comand == 'p':
    print(get_people_name(documents))
    
  elif comand == 's':
    print(get_shelf_number(directories))
    
  elif comand == 'l':
    (get_list(documents))
    
  elif comand == 'a':
    print(add_doc(directories))