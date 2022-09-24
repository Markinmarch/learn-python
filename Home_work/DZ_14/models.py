import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# создание таблицы Publisher
class Publisher(Base):
    __tablename__ = 'publisher'
    
    # мне пришлось типу данных id присвоить str, так как тогда функция who_sells() не работала бы, согласно заданию
    # а именно при вводе или id, или name выдавалась ошибка, что id не может быть str, а name не может быть int
    id = sq.Column(sq.String, primary_key = True)
    name = sq.Column(sq.String(length = 40), unique = True)
    
    # изменяем тип str в более читабельный вид
    def __str__(self):
        return f'{self.id}: {self.name}'

# создание таблицы Book    
class Book(Base):
    __tablename__ = 'book'
    
    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length = 40), unique = True)
    # соответственно с предыдущим комментарием, тут тоже пришлось изменить тип данных id на str
    id_publisher = sq.Column(sq.String, sq.ForeignKey('publisher.id'), nullable = False)
    
    publisher = relationship(Publisher, backref = 'book')
    
    def __str__(self):
        return f'{self.id}: {[self.title, self.id_publisher]}'

# создание таблицы Shop    
class Shop(Base):
    __tablename__ = 'shop'
    
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 40), unique = True)
    
    def __str__(self):
        return f'{self.id}: {self.name}'

# создание таблицы Stock    
class Stock(Base):
    __tablename__ = 'stock'
    
    id = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable = False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable = False)
    count = sq.Column(sq.Integer, nullable = True)
    
    book = relationship(Book, backref = 'stock')
    shop = relationship(Shop, backref = 'stock')
    
    def __str__(self):
        return f'{self.id}: {[self.id_book, self.id_shop, self.count]}'

# создание таблицы Sale    
class Sale(Base):
    __tablename__ = 'sale'
    
    id = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.String, nullable = True)
    date_sale = sq.Column(sq.String, nullable = True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable = False)
    count = sq.Column(sq.Integer, nullable = True)
    
    stock = relationship(Stock, backref = 'sale')
    
    def __str__(self):
        return f'{self.id}: {[self.price, self.date_sale, self.id_stock, self.count]}'
    
def create_table(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    