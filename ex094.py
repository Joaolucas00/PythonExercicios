pessoas = {}
pessoal = []
cont = 0
while True:
    pessoas.clear()
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo [M/F]:').upper()[0]
        if pessoas['sexo'] in 'MF':
            if pessoas['sexo'] == 'F':
                cont += 1
            break
        else:
            print('ERRO! Coloque apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    pessoal.append(pessoas.copy())
    while True:
        continuar = input('Quer continuar? [S/N]: ').upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Coloque apenas S ou N.')
    if continuar in 'N':
        break
print('-='*25)
soma = []
for p in pessoal:
    soma.append(p['idade'])
média = sum(soma)/len(pessoal)
print(f'Ao todo temos {len(pessoal)} pessoas cadastradas.')
print(f'A média de idade é de {média:.2f}')
print(f'Temos {cont} mulheres cadastradas e elas são: ', end='')
for p in pessoal:
    if p['sexo'] == 'F':
        print(f'[{p["nome"]}]', end='...')
print('\nAs pessoas acima da méida são: ')
for p in pessoal:
    if p['idade'] >= média:
        print('  ')
        for k, v in p.items():
            print(f' {k} é {v}', end=';')
        print()
print('-'*20)
print('\n   <<< ENCERRADO >>>')
