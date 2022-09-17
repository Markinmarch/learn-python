import requests

hero_nick = ['Hulk', 'Captain America', 'Thanos']
hero_skill = 'intelligence'
url_adress = 'https://akabab.github.io/superhero-api/api/all.json'

# Делаем запрос по адресу
def makea_request(url):
    take_info = requests.get(url).json()
    return take_info
ready_info = makea_request(url_adress)

# Вытаскиваем данные по именам*
# * можно вписать любые другие имена в переменную hero_nick
def extracting_a_value_by_name(nickname, skill):
    hero_list_stats = []
    hero_list_name = []
    for hero in ready_info:
        for one_nick in nickname:
            if hero.get('name') == one_nick:
                for k, v in hero['powerstats'].items():
                    if k == skill:
                        hero_list_name.append(hero['name'])
                        hero_list_stats.append(v)
    return hero_list_name, hero_list_stats
ready_hero = extracting_a_value_by_name(hero_nick, hero_skill)
# print(ready_hero)

# Создаём словарь
def creat_dict(ready_list):
    ready_hero_dict = dict(zip(ready_list[0], ready_list[1]))
    return ready_hero_dict
ready_hero_dict = creat_dict(ready_hero)
# print(ready_hero_dict)

#Определяем самого умного* персонажа
# *тут можно подставить любую другую характеристику персонажа в переменной hero_skill
def who_is_the_coolest(given_ready_dict):
    return max(given_ready_dict, key=given_ready_dict.get)
he_is_coolest = who_is_the_coolest(ready_hero_dict)

print(f'Самым умным персонажем оказался {he_is_coolest}')