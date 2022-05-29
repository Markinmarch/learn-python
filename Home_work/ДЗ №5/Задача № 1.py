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

def add_doc(docs_add, direct_add):
  num_shelf = input('Введите номер полки, куда положить документ: ')
  if num_shelf not in direct_add.keys():
      print('Такой полки не существует!')
  else:
      print('Готово!')
  new_data = {}
  for Ddata in ('type', 'number', 'name'):
      new_data[Ddata] = input(f'Введите данные: {Ddata}')
  docs_add.append(new_data)
  direct_add[num_shelf] = [new_data['number']]
  for doc in docs_add:
      print(doc['type'], doc['number'], doc['name'])
  print(direct_add)
# add_doc(documents, directories)

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
    add_doc(documents, directories)