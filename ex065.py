print('→'*3, 'Super calculadora de média aritimética', '←'*3)
print('-'*50)
cont = 0
soma = 0
SouN = 'S'
maior = menor = 0
while SouN == 'S':
    núm = float(input('Digite um número:'))
    SouN = str(input('Quer continuar[S/N]?').upper())
    cont += 1
    soma += núm
    if cont == 1:
        maior = núm
        menor = núm
    else:
        if núm >= maior:
            maior = núm
        else:
            if núm <= menor:
                menor = núm
print('~' * 40)
print('Você digitou {} números e a média dos número digitados foi {:.2f}.'.format(cont, soma / cont))
print('O menor valor foi {} e o maior valor foi {}.'.format(menor, maior))
