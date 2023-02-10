lista = []
while True:
    elem = int(input('Digite um número para a lista: '))
    if elem in lista:
        print('Valor repitido. Não vou adicionar...')
    else:
        lista.append(elem)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] :').upper().strip()[0]
    if continuar in 'N':
        break
lista.sort()
print('-='*30)
print(f'A lista foi: {lista}')
