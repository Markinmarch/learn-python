# получаем response body

import requests
url = 'https://httpbin.org/get'
resp = requests.get(url)
print(resp.json())

# получаем response text

r = requests.get('https://netology.ru/')
print(r.json())