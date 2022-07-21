import requests

hero_nick = ['Hulk', 'Captain America', 'Thanos']
hero_skill = 'intelligence'
url_adress = 'https://akabab.github.io/superhero-api/api/all.json'

# Делаем запрос по адресу
def makea_request(url):
    take_info = requests.get(url).json()
    return take_info
ready_info = makea_request(url_adress)

# Вытаскиваем данные по именам и выделяем с максимальным скиллом
def extracting_a_value_by_name(nickname, skill):
    for hero in ready_info:
        for one_nick in nickname:
            if hero.get('name') == one_nick:
                for k, v in hero['powerstats'].items():
                    if k == skill:
                        print(hero['name'], ':', k, '=', v)
ready_hero = extracting_a_value_by_name(hero_nick, hero_skill)
