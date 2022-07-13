import csv

def open_file(file_name):
    with open(file_name, 'r', encoding='1252') as file:
        ready_to_read = csv.reader(file, delimiter=',')
        return ready_to_read
adress = 'C:/Users/User/Desktop/Study/netology_learning/Home_work/Formats/glff.csv'
open_file(adress)
