import dbm
from application import salary
from application.db import people
import datetime

print(datetime.datetime.now())

if __name__ == '__main__':
    
    print(salary.calculate_salary())
    print(people.get_employees())
