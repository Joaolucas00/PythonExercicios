from random import randint
from time import sleep
jogadas = []
sorteio = []
print('-'*40, f'\n{"JOGA NA MEGA SENA":^40}')
print('-'*40)
jogos = int(input('Quantos jogos você quer mostrar? '))
print('-='*4, f'{f"SORTEANDO {jogos} JOGOS"}', '-='*4)
for d in range(0, jogos):
    for c in range(0, 6):
        núm = randint(1, 60)
        if núm not in sorteio:
            sorteio.append(núm)
        else:
            while True:
                núm = randint(1, 60)
                if núm not in sorteio:
                    sorteio.append(núm)
                    break
    jogadas.append(sorteio[:])
    sorteio.clear()
    jogadas[d].sort()
    print(f'Jogo {d + 1}: {jogadas[d]}')
    sleep(0.5)
print('-='*4, '< BOA SORTE! >', '-='*4)
