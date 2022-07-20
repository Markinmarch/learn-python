hero_nick = ['Hulk', 'Capitan America', 'Thanos']
hero_skill = 'intelligence'

def who_is_smart(nick, skill):
    import requests
    url = 'https://akabab.github.io/superhero-api/api'
    take_info = requests.get(url).json()
    print(take_info)
# who_is_smart(hero_nick, hero_skill)