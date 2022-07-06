from fileinput import filename


catal_ad = 'Home_work/DZ №7/text/'

def mod_os(adress):
    import os
    file_list = os.listdir(adress)
    return file_list

file_list = mod_os(catal_ad)

def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def sort_ready_text(lst, adress):
    read = [open_file(adress + lst[i]) for i in range(0, len(lst))]
    print(filename(read))
    ready_text = sorted(read, key = len)
    return '\n'.join(ready_text)
read = sort_ready_text(file_list, catal_ad)
# print(read)

def write_file(ready_file):
    with open(r'Home_work/DZ №7/new_file.txt', 'w', encoding='utf-8') as file:
        return file.write(ready_file)

write_file(read)

# print(how_lines(read))