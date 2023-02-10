from random import randint
cont = 0
print('-='*20)
print('Vamos jogar Par ou Ípar!')
print('-='*20)
while True:
    pc = int(randint(1, 10))
    jogador = int(input('Diga um valor:'))
    PouI = ' '
    vs = jogador + pc
    while PouI not in 'PI':
        PouI = str(input('Par ou Ípar? [P/I]:').upper().strip()[0])
    print('-' * 50)
    print(f'Você jogou {jogador} e o computador {pc}! O total deu {vs}!')
    if vs % 2 == 0 and PouI == 'P':
        print('Deu Par!')
        print('-' * 50)
        print('Jogador VENCEU!')
        print('Vamos jogar de novo...')
        print('-=' * 20)
        cont += 1
    elif vs % 2 != 0 and PouI == 'I':
        print('Deu Ímpar!')
        print('-' * 50)
        print('Jogador VENCEU!')
        print('Vamos jogar de novo...')
        print('-=' * 20)
        cont += 1
    elif vs % 2 != 0 and PouI == 'P':
        print('Deu Ímpar!')
        print('-' * 50)
        print('Jogador PERDEU!')
        print('-=' * 20)
        break
    elif vs % 2 == 0 and PouI == 'I':
        print('Deu Par!')
        print('-' * 50)
        print('Jogador PERDEU!')
        print('-='*20)
        break
print(f'GAME OVER! Você venceu {cont} vezes.')