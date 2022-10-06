class FlatIterator:

    def __init__(self, multi_list):
        """Метод определяет атрибут для хранения списка списков"""
        self.multi_list = multi_list

    def __iter__(self):
        """Метод определяет атрибуты для итерации по списку"""
        self.list_iter = iter(self.multi_list)
        self.nested_list = []
        self.cursor = -1
        return self

    def __next__(self):
        """Метод определяет и возвращает следущий элемент списка списков"""
        self.cursor += 1
        if len(self.nested_list) == self.cursor:
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iter)
        return self.nested_list[self.cursor]

# функция позволяет возвращать эелементы из списка списков с двойным уровнем вложености
def flat_generator(my_list):
    
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(f'{item}')

    flat_list = [item for item in FlatIterator(nested_list)]
    print(f'\n{flat_list}\n')

    for item in flat_generator(nested_list):
        print(item)