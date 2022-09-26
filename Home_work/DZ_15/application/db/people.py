def get_employees():
    
    return '9999999'

# Мне просто жаль удалять написанный код ниже

# import sqlalchemy
# import sqlalchemy as sq
# from sqlalchemy.orm import sessionmaker, declarative_base, relationship
# import getpass

# DB_type = input('Введите тип БД для подключения(например postgresql): ')
# DB_name = input('Введите имя БД: ')
# user_name = input('Введите имя пользователя БД: ')
# user_pass = getpass.getpass('Введите пароль от БД: ')

# DSN = f'{DB_type}://{user_name}:{user_pass}@localhost:5432/{DB_name}'
# # DSN = f'postgresql://postgres:***@localhost:5432/DZ_15'
# engine = sqlalchemy.create_engine(DSN)
# Base = declarative_base()

# Session = sessionmaker(bind = engine)
# session = Session()

# # создание таблицы Employee
# class Employee(Base):
#     __tablename__ = 'employee'

#     id = sq.Column(sq.Integer, primary_key = True)
#     name = sq.Column(sq.String(length = 40), nullable = False)
#     last_name = sq.Column(sq.String(length = 40), nullable = False)
    
#     # homeworks = relationship("Homework", back_populates="course")

#     # изменяем тип str в более читабельный вид
#     def __str__(self):
#         return f'{self.id}: {self.name} {self.last_name}'

# # создание таблицы Salary    
# class Salary(Base):
#     __tablename__ = 'salary'
    
#     id = sq.Column(sq.Integer, primary_key = True)
#     experience = sq.Column(sq.Integer, nullable = False)
#     allowance = sq.Column(sq.Float, nullable = False)
#     base_salary = sq.Column(sq.Float, nullable = False)
#     salary = sq.Column(sq.Float, nullable = False)
#     id_employee = sq.Column(sq.Integer, sq.ForeignKey('employee.id'), nullable = False)

#     employee = relationship(Employee, backref = 'salary')

#     def __str__(self):
#         return f'{self.id}: {[self.salary, self.experience, self.allowance]}'

# # создание таблиц
# def get_create_table(engine):
#     Base.metadata.create_all(engine)
#     # Base.metadata.drop_all(engine)
# get_create_table(engine)


# # функция ввода в БВ данных
# def data_entry():

#     name_employee = input('Ввод имени и фамилии: ').split(' ')
#     total = float(input('Ввод ЗП:'))
#     exp = int(input('Опыт работы: '))
#     koef = float(input('Повышающий коэффициент: '))
#     e = Employee(name = name_employee[0], last_name = name_employee[1])
#     session.add(e)
#     s = Salary(base_salary = total, salary = total*koef, experience = exp/12, allowance = koef, employee = e)
#     session.add(s)
#     session.commit()
#     session.close()
#     print('Готово!')

# data_entry()