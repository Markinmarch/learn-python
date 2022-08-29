import csv

def read_file_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        ready_to_read = csv.reader(file, delimiter=',')
        return ready_to_read
adress = 'C:/Users/User/Desktop/Study/netology_learning/Home_work/Formats/CSV/auto.csv'
# read_file_csv(adress)
# res = ['user_name', 'user_age', 'user_gender']
def  write_file_csv(new_file):
    with open(new_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerows([
            ['user_name', 'user_age', 'user_gender']
            ]
        )
new_adress = 'C:/Users/User/Desktop/Study/netology_learning/Home_work/Formats/CSV/new_file.csv'
# write_file_csv(new_adress)

def append_datas_users_csv(main_file):
    name = input('Введите имя: ')
    age = int(input('Введите количество полных лет: '))
    gender = input('Введите свой пол (Например: male/famale):')
    with open(main_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            [name,age,gender]
        )

append_datas_users_csv(new_adress)