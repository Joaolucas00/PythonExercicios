pessoal = []
dados = []
maior = menor = cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoal.append(dados[:])
    dados.clear()
    print(pessoal)
    cntinuar = str(input('Quer continuar? [S/N]: ').strip()[0])
    if cntinuar in 'Nn':
        break
print('-='*20)
print(f'No total, foi {len(pessoal)} pessoas cadastradas.')
for p in pessoal:
    cont += 1
    if cont == 1:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] >= maior:
            maior = p[1]
        else:
            if p[1] <= menor:
                menor = p[1]
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoal:
    if p[1] == maior:
        print(f'[{p[0]}].', end=' ')
print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoal:
    if p[1] == menor:
        print(f'[{p[0]}].', end=' ')
