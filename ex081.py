lista = []
while True:
    lista.append(int(input('Digite um número:')))
    continuar = str(input('Quer continuar? [S/N]: ').upper().strip()[0])
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os números em ordem decrecente são {lista}.')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não  está na lista!')
