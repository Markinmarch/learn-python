import json


path = 'C:/Users/User/Desktop/Study/netology_learning/Home_work/DZ_14/data.json'
open_file = json.load(open(path, 'r', encoding='utf-8'))

def get_key(value):
    
    for main_item in open_file:
        if main_item.get('model') == value:
            print(main_item)

get_key('publisher')