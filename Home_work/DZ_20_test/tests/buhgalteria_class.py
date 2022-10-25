from data import buh_data

class Buhgalteria():
    '''основной метод, который определяет переменные и функции'''
    def __init__(self,
                 name = buh_data.documents,
                 shelf_number = buh_data.directories,
                 docs = buh_data.documents,
                 docs_add = buh_data.documents,
                 direct_add = buh_data.directories
                 ):
        self.name = name
        self.shelf_number = shelf_number
        self.docs = docs
        self.docs_add = docs_add
        self.direct_add = direct_add

    def get_people_name(self, what_number_doc):
        # what_number_doc = input('Введите номер документа: ')
        for people in self.name:
            if what_number_doc in people['number']:
                return(people['name'])
        return('Номера не существует!')
    
    def get_shelf_number(self, what_number_doc):
        # what_number_doc = input('Введите номер документа: ')
        for shelf_value in self.shelf_number:
            if what_number_doc in self.shelf_number.get(shelf_value):
                return(f'Документ находится на полке № {shelf_value[0]}')
        return('Отсутствуют документы с данным номером!')
        
    def get_list(self):
        lst = []
        for doc in self.docs:
            ien = f"{doc['type']} {doc['number']} {doc['name']}"
            lst.append(ien)
        return lst
        
    def add_doc(self, num_shelf, new_data):
        # num_shelf = input('Введите номер полки, куда положить документ: ')
        if num_shelf not in self.direct_add.keys():
            return 'Такой полки не существует!'
        new_data = {}
        # for Ddata in ('type', 'number', 'name'):
            # new_data[Ddata] = input(f'Введите данные: {Ddata}')
        self.docs_add.append(new_data)
        self.direct_add[num_shelf].append(new_data['number'])
        for doc in self.docs_add:
            return f"{doc['type'], doc['number'], doc['name']}"
        return self.direct_add
    
class work_buh():
    '''рабочий метод, в котором вводится команда'''
    
    def get_input(self, text):
        return input(text)
    
    documents = buh_data.documents
    directories = buh_data.directories
        
    get_args_to_class = Buhgalteria(
    documents,
    directories,
    documents,
    documents,
    directories
    )
    def huef(self):
        while True:
            print('Возможные команды: p, s, l, a')
            comand = input('Введите название команды ')
            if comand == 'p':
                comand_p = Buhgalteria.get_people_name(self.get_args_to_class, input('Введите номер документа: '))
                return comand_p
            elif comand == 's':
                comand_s = Buhgalteria.get_shelf_number(self.get_args_to_class, input('Введите номер документа: '))
                return comand_s
            elif comand == 'l':
                comand_l = Buhgalteria.get_list(self.get_args_to_class)
                return comand_l
            elif comand == 'a':
                data_lst = []
                for Ddata in ('type ', 'number ', 'name '):
                    Ddata = input(f'Введите данные: {Ddata}')
                comand_a = Buhgalteria.add_doc(self.get_args_to_class, input('Введите номер полки, куда положить документ: '), Ddata)
                return comand_a
            # break
    