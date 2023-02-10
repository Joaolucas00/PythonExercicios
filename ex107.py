import moeda
n1 = float(input('Digite o preço: R$'))
print(f'A metade de R${n1} é {moeda.metade(n1)}')
print(f'O dobro de {n1} é {moeda.dobro(n1)}')
print(f'Um aumento de 10% de {n1} é {moeda.aumento(n1, 10)}')
