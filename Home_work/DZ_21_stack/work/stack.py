class myStack():
    
    def __init__(self, stack_data, something):
        self.SD = stack_data
        self.SMTG = something
    
    # проверка на пустоту    
    def isEmpty(self):
        return not(bool(self.SD))
    
    # добавляет новый элемент
    def push(self):
        self.SD.append(self.SMTG)
    
    # удаляет верхний элемент
    def pop(self):
        self.SD.pop[-1]
    
    # возвращает верхний элемент
    def peek(self):
        return self.SD[-1]
    
    # возвращает количество элементов
    def size(self):
        return len(self.SD)
    
class getIt(myStack):
    
    def __init__(self, stack_data, something):
        super().__init__(stack_data, something)
    
    # проверка на сбалансированость
    def check_ballance(self, item):
        while '[]' in item or '()' in item or '{}' in item:
            item = item.replace('[]', '')
            item = item.replace('()', '')
            item = item.replace('{}', '')
        if bool(item) == False:
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'
                
    

            
