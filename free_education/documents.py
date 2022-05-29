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

# num_shelf = input('Введите номер полки, куда положить документ. ')
# if num_shelf not in directories.keys():
#     print('Такой полки не существует!')
# else:
#     print('Готово!')
# new_data = {}
# for Ddata in ('type', 'number', 'name'):
#     new_data[Ddata] = input(f'Введите данные: {Ddata}')
# documents.append(new_data)
# directories[num_shelf] = new_data['number']
# for doc in documents:
#     print(doc['type'], doc['number'], doc['name'])
# print(directories)

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
print(del_doc(documents, directories))