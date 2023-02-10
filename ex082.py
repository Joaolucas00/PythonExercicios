lista = list()
pares = list()
ímpares = list()
while True:
   lista.append(int(input('Digite um número: ')))
   continuar = str(input('Quer continuar? [S/N]').strip()[0])
   if continuar in 'Nn':
       break
print('-='*30)
print(f'A lista completa é {lista}.')
for l in lista:
    if l % 2 == 0:
        pares.append(l)
    else:
        ímpares.append(l)
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {ímpares}.')

'''
Outra solução...
print(f'A lista completa é {lista}')
print('A lista de pares é:', end=' ')
for par in lista:
    if par % 2 == 0:
        print(par, end=', ')
print('\nA lista de ímpares é: ', end=' ')
for ímpar in lista:
    if ímpar % 2 != 0:
        print(ímpar, end=', ')
'''