import itertools

def stroka(argum):

    stroka_iz_spiskov = itertools.chain(argum[0], argum[1], argum[2])
    print(*stroka_iz_spiskov)

def spisok(argum):
    
    bolshoi_spisok = itertools.chain(argum[0], argum[1], argum[2])
    print(list(bolshoi_spisok))

