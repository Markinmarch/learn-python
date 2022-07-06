catal_ad = 'Home_work/DZ №7/text/'

def mod_os(adress):
    import os
    file_list = os.listdir(adress)
    return file_list

file_list = mod_os(catal_ad)

def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


for i in range(0, len(file_list)):
    read = open_file(catal_ad + file_list[i])
    


def how_lines(file):
    return len(file.strip().split('\n'))

# print(how_lines(read))