list_ = ['2018-01-01', 'yandex', 'cpc', 100]
list_1 = {list_[2]: list_[3]}
list_2 = {list_[1]: list_1}
list_3 = {list_[0]: list_2}

print(list_ready := list_3)
