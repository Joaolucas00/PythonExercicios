matriz = [[], [], []]
pares = []
somap = maior = 0
print(f'-'*40, f'\n{"GERADOR DE MATRIZ":^40}')
print('-'*40)
for c in range(0, 3):
    linha0 = int(input(f'Digite um número para a matriz [0, {c}]: '))
    if linha0 % 2 == 0:
        pares.append(linha0)
    matriz[0].append(linha0)
for c in range(0, 3):
    linha1 = int(input(f'Digite um número para a matriz [1, {c}]: '))
    if c == 0:
        maior = linha1
    else:
        if linha1 >= maior:
            maior = linha1
    if linha1 % 2 == 0:
        pares.append(linha1)
    matriz[1].append(linha1)
for c in range(0, 3):
    linha2 = int(input(f'Digite um número para a matriz [2, {c}]: '))
    if linha2 % 2 == 0:
        pares.append(linha2)
    matriz[2].append(linha2)
print('-='*30)
print(f'[{matriz[0][0]:^5}] [{matriz[0][1]:^5}] [{matriz[0][2]:^5}]\n'
      f'[{matriz[1][0]:^5}] [{matriz[1][1]:^5}] [{matriz[1][2]:^5}]\n'
      f'[{matriz[2][0]:^5}] [{matriz[2][1]:^5}] [{matriz[2][2]:^5}]')
print('-='*30)
for p in pares:
    somap += p
print(f'A soma de todos os números pares é {somap}.')
print(f'A soma da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior número da segunda linha é {maior}.')