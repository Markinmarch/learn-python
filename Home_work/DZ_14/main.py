from operator import or_
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_table, Publisher, Book, Shop, Stock, Sale
import getpass
import json

DB_type = input('Введите тип БД для подключения(например postgresql): ')
DB_name = input('Введите имя БД: ')
user_name = input('Введите имя пользователя БД: ')
user_pass = getpass.getpass('Введите пароль от БД: ')

DSN = f'{DB_type}://{user_name}:{user_pass}@localhost:5432/{DB_name}'
# DSN = f'postgresql://postgres:***@localhost:5432/HW_14'
engine = sqlalchemy.create_engine(DSN)
create_table(engine)

Session = sessionmaker(bind = engine)
session = Session()

# функция импортирования модели БД
def import_models():
    
    path = input('Введите путь к импортируемым данным: ')
    # path = 'C:/Users/User/Desktop/Study/netology_learning/Home_work/DZ_14/data.json'
    open_file = json.load(open(path, 'r', encoding='utf-8'))
    for item in open_file:
        
        if item.get('model') == 'publisher':
            session.add(
                Publisher(
                id = item.get('pk'),
                name = item.get('fields').get('name')
                ))
            
        elif item.get('model') == 'book':
            session.add(
                Book(
                    id = item.get('pk'),
                    title = item.get('fields').get('title'),
                    id_publisher = item.get('fields').get('id_publisher')
                )
            )
            
        elif item.get('model') == 'shop':
            session.add(
                Shop(
                id = item.get('pk'),
                name = item.get('fields').get('name') 
                ))
            
        elif item.get('model') == 'stock':
            session.add(
                Stock(
                id = item.get('pk'),
                id_book = item.get('fields').get('id_book'),
                id_shop = item.get('fields').get('id_shop'),
                count = item.get('fields').get('count')
                ))
            
        elif item.get('model') == 'sale':
            session.add(
                Sale(
                id = item.get('pk'),
                price = item.get('fields').get('price'),
                date_sale = item.get('fields').get('date_sale'),
                id_stock = item.get('fields').get('id_stock'),
                count = item.get('fields').get('count')
                ))
            
            session.commit()
            session.close()

import_models()


# функция нахождения магазинов по целевому издателю
def who_sells():
    
    lst = []
    who = input('Введите имя или id издателя: ')     
    #поиск издателя по значению 
    publisher = session.query(Publisher).filter(or_(Publisher.id == who, Publisher.name == who))
    for item_publisher in publisher.all():
        # объединяем столбцы stock и book, по Book.id_publisher находим id_shop нужных магазинов
        stock = session.query(Stock).join(Book).filter(Book.id_publisher == item_publisher.id)
        for item_stock in stock.all():
            # в таблице shop находим необходимые магазины по item_stock.id_shop
            shop = session.query(Shop).filter(Shop.id == item_stock.id_shop)
            for item_shop in shop.all():
                # и приводим всё в красивый вид
                lst.append(item_shop.name)
                ready_list = ', '.join(set(lst))

    return f'Магазины, продающие издательство {item_publisher.name}: {ready_list}'

print(who_sells())