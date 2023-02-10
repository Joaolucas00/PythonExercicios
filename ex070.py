cont2 = total = cont = maior = menor = 0
continuar = produto = nome = nomemaior  = ' '
print('-'*20)
print('      Lojinha')
print('-'*20)
while True:
    produto = str(input('Nome do produto:'))
    valor = float(input('Preço do produto: R$'))
    cont += 1
    total += valor
    if valor >= 1000:
        cont2 += 1
    if cont == 1:
        maior = valor
        menor = valor
        nome = produto
        nomemaior = produto
    else:
        if valor >= maior:
            maior = valor
            nomemaior = produto
        else:
            if valor <= menor:
                menor = valor
                nome = produto
    while True:
        continuar = str(input('Quer continuar? [S/N] :').upper().strip()[0])
        if continuar in 'S' or continuar in 'N':
            break
    if continuar in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {cont2} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nome} que custou {menor} e o maior foi {nomemaior} que custou R${maior:.2f}')
