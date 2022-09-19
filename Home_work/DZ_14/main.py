import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_table, Course, Homework

DSN = 'postgresql://postgres:M4rk130t08@localhost:5432/HW_14'
engine = sqlalchemy.create_engine(DSN)

create_table(engine)

Session = sessionmaker(bind = engine)
session = Session()

course1 = Course(name = 'Python')
# print(course1.id)
session.add(course1)
session.commit()
print(course1.id)
print(course1)

session.close()