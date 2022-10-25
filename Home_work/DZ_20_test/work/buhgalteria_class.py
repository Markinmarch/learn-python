from data import buh_data
    
def get_input(text):
    return input(text)

class Buhgalteria():
    '''основной метод, который определяет переменные и функции'''
    def __init__(self,
                 name,
                 shelf_number,
                 docs,
                 docs_add,
                 direct_add):
        self.name = name
        self.shelf_number = shelf_number
        self.docs = docs
        self.docs_add = docs_add
        self.direct_add = direct_add

    def get_people_name(self):
        what_number_doc = get_input('Введите номер документа: ')
        for people in self.name:
            if what_number_doc in people['number']:
                return(people['name'])
        return('Номера не существует!')
    
    def get_shelf_number(self):
        what_number_doc = get_input('Введите номер документа: ')
        for shelf_value in self.shelf_number:
            if what_number_doc in self.shelf_number.get(shelf_value):
                return(f'Документ находится на полке № {shelf_value[0]}')
            return('Отсутствуют документы с данным номером!')
        
    def get_list(self):
        for doc in self.docs:
            return f"{doc['type']} {doc['number']} {doc['name']}"
        
    def add_doc(self):
        num_shelf = get_input('Введите номер полки, куда положить документ: ')
        if num_shelf not in self.direct_add.keys():
            return 'Такой полки не существует!'
        new_data = {}
        for Ddata in ('type', 'number', 'name'):
            new_data[Ddata] = get_input(f'Введите данные: {Ddata}')
        self.docs_add.append(new_data)
        self.direct_add[num_shelf].append(new_data['number'])
        for doc in self.docs_add:
            print(doc['type'], doc['number'], doc['name'])
        return self.direct_add
    
class work_buh():
    '''рабочий метод, в котором вводится команда'''
    documents = buh_data.documents
    directories = buh_data.directories
    
    get_args_to_class = Buhgalteria(
    documents,
    directories,
    documents,
    documents,
    directories
    )

    while True:
        print('Возможные команды: p, s, l, a')
        comand = get_input('Введите название команды ')
        if comand == 'p':
            print(Buhgalteria.get_people_name(get_args_to_class))
        elif comand == 's':
            print(Buhgalteria.get_shelf_number(get_args_to_class))
        elif comand == 'l':
            print(Buhgalteria.get_list(get_args_to_class))
        elif comand == 'a':
            print(Buhgalteria.add_doc(get_args_to_class))
        break
    