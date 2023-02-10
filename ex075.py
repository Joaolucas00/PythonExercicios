numeros = (int(input('Digite um número:')), int(input('Digite um número:')),
           int(input('Digite um número:')), int(input('Digite um número:')))
print(f'Você digitou os números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('Não temos o valor 3 no conjunto')
print('Pares digitados:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
