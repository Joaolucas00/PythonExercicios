from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
print('Valores sorteados:')
for c in range(0, 4):
    jogo[f'jogador{c+1}'] = randint(1, 6)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
cont = 0
print('-='*20)
print('     == RANKING DOS JOGADORES ==')
for k, v in ranking:
    cont += 1
    print(f'   {cont} lugar: {k} com {v}')
    sleep(1)
