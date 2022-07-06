catal_ad = 'Home_work/DZ №7/text/'

def mod_os(adress):
    import os
    file_list = os.listdir(adress)
    return file_list

file_list = mod_os(catal_ad)

def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def huef(lst, adress):
    for i in range(0, len(lst)):
        read = open_file(adress + lst[i])
        print(read)
read = huef(file_list, catal_ad)

# def how_lines(read):
#     return str(read)
# how_lines(read)

# print(how_lines(read))