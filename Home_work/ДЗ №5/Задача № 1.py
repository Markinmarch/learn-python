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
  for shelf_num in shelf_number:
    return shelf_number.keys()
print(get_shelf_number(directories))


