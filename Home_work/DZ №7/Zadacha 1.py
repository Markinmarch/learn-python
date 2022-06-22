def open_file(txt_file):
    with open(txt_file, 'r', encoding='utf=8') as file:
        return file.read()

