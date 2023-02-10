import moeda
n1 = float(input('Digite o preço: R$').replace(',', '.'))
print(f'A metade de {moeda.moeda(n1)} é {moeda.moeda(moeda.metade(n1))}')
print(f'O dobro de {moeda.moeda(n1)} é {moeda.moeda(moeda.dobro(n1))}')
print(f'Um aumento de 10% de {moeda.moeda(n1)} é {moeda.moeda(moeda.aumento(n1, 10))}')
