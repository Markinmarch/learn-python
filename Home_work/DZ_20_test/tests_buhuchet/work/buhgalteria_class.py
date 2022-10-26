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
        for people in self.name:
            if what_number_doc in people['number']:
                return(people['name'])
        return('Номера не существует!')
    
    def get_shelf_number(self, what_number_doc):
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
        
    def add_doc(self, new_data, num_shelf):
        if num_shelf not in self.direct_add.keys():
            return 'Такой полки не существует!'
        self.docs_add.append(new_data)
        self.direct_add[num_shelf].append(new_data['number'])
        lst = []
        for dok in self.docs_add:
            cen = f"{dok['type']} {dok['number']} {dok['name']}"
            lst.append(cen)
        return lst, self.direct_add
    
class work_buh(Buhgalteria):
    '''рабочий метод, в котором вводится команда'''
    
    def __init__(self, name=buh_data.documents, shelf_number=buh_data.directories, docs=buh_data.documents, docs_add=buh_data.documents, direct_add=buh_data.directories):
        super().__init__(name, shelf_number, docs, docs_add, direct_add)
    
    def get_input(self, text):
        return input(text)

    def get_command(self):
        while True:
            print('Возможные команды: p, s, l, a')
            comand = input('Введите название команды ')
            if comand == 'p':
                comand_p = self.get_people_name(input('Введите номер документа: '))
                return comand_p
            elif comand == 's':
                comand_s = self.get_shelf_number(input('Введите номер документа: '))
                return comand_s
            elif comand == 'l':
                comand_l = self.get_list()
                return comand_l
            elif comand == 'a':
                new_data = {}
                for Ddata in ('type', 'number', 'name'):
                    new_data[Ddata] = input(f'Введите данные: {Ddata}')
                comand_a = self.add_doc(new_data, input('Введите номер полки, куда положить документ: '))
                return comand_a
            # break
    