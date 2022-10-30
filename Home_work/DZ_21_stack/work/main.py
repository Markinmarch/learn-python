from stack import myStack, getIt
from data import BALLANCED_DATA, UNBALLANCED_DATA, EMPTY_DATA

if __name__ == '__main__':
    # проверяем сбалансированность
    for item in BALLANCED_DATA + UNBALLANCED_DATA:
        print(f'{item:10} -> {getIt(BALLANCED_DATA + UNBALLANCED_DATA, 1).check_ballance(item)}')
    
    # проверка на пустоту
    print(myStack(EMPTY_DATA, None).isEmpty())
    # добавляем элемент к пустому списку
    myStack(EMPTY_DATA, '[[]()([[]])]').push()
    # проверяем наличие изменений
    print(EMPTY_DATA)
    # и снова проверяем на пустоту
    print(myStack(EMPTY_DATA, 1).isEmpty())