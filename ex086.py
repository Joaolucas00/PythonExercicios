matriz = [[], [], []]
print(f'-'*40, f'\n{"GERADOR DE MATRIZ":^40}')
print('-'*40)
for c in range(0, 3):
    linha0 = int(input(f'Digite um número para a matriz [0, {c}]: '))
    matriz[0].append(linha0)
for c in range(0, 3):
    linha1 = int(input(f'Digite um número para a matriz [1, {c}]: '))
    matriz[1].append(linha1)
for c in range(0, 3):
    linha2 = int(input(f'Digite um número para a matriz [2, {c}]: '))
    matriz[2].append(linha2)
print('-='*30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]\n'
      f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]\n'
      f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')


'''
Outra solução:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a [{l, c}]'))
print('-='*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        print()
'''