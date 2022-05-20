queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

storage = {}

for query in queries:
    words = query.split()

    if len(words) in storage.keys():
        storage[len(words)] += 1
    else:
        storage[len(words)] = 1

for key, value in storage.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слов: {percentage}% ({value} запр.)')