#Код исключительно для проб, не является рабочим объектом
from os import link
import requests

link = 'http://icanhazip.com/'
take = str(requests.get(link))
print(f'Ваш ip-адрес: {take.text}')
print(f'Ваш статус: {take.status_code}')

with open('l.html', 'w', encoding = 'UTF-8') as file:
   file.write(take) 