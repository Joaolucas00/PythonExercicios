número = cont = soma = 0
while número != 999:
    número = int(input('Digite um número[999 para parar]:'))
    soma = soma + número
    cont += 1
print('Total de valores digitados foi {}, e a soma entre eles foi {}.'.format(cont - 1, soma - 999))
