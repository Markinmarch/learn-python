def open_file():
    with open('DZ №7\dish_list.txt', 'r', encoding='utf-8') as file:
        txt = {file.read()}
        print(txt)
        return

open_file()

def data_structure():
    cook_book = {
        open_file
    }
    print(cook_book)

data_structure()