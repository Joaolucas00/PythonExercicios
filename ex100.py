from random import randint
from time import sleep


def sortear(lst):
    while True:
        num = randint(0,  10)
        if num not in lst:
            lst.append(num)
        if len(lst) == 5:
            break
    for elem in lst:
        sleep(0.5)
        print(elem, end=' ')


def somap(par):
    pares = []
    for elem in par:
        if elem % 2 == 0:
            pares.append(elem)
    print(f'{sum(pares)}.')


valores = []
print(f'Sorteando 5 valores da lista: ', end=' ')
sortear(lst=valores)
print('\nA soma de todos os números pares da lista é ', end='')
somap(par=valores)
