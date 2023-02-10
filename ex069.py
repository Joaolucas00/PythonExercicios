adultos = 0
homens = 0
mulheres = 0
while True:
    print('-'*25, '\n  Cadastre uma pessoa')
    print('-'*25)
    #nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F] :').upper().strip()[0])
    if sexo in 'M':
        homens += 1
    if idade < 20 and sexo in 'F':
        mulheres += 1
    if idade >= 18:
        adultos += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]').upper().strip()[0])
        print('-='*15)
    if continuar in 'N':
        break
print(f'O total de pessoas com mais de 18 anos foi {adultos}.')
print(f'Ao todo temos {homens} homens.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')