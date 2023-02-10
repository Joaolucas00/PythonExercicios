print('Gerador de PA. \n-=-=-=-=-=-=-=-=-=-=')
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
cont = 1
while cont <= 10:
    print('{}'.format(primeiro), end=' -> ')
    primeiro = primeiro + razão
    cont = cont + 1
#print('total de termos utilizados: {}'.format(cont - 1))
#for c in range(1, 1000):
v1 = 1
while v1 != 0:
    v1 = int(input('Quantos termos você quer mostrar mais?'))
    contv1 = cont + v1
    while cont <= contv1 - 1:
        print(primeiro, end=' -> ')
        primeiro = primeiro + razão
        cont = cont + 1
    #if v1 == 0:
print('Progreção finalizada. Total de termos utilizados: {}'.format(cont - 1))
print('FIM.')



'''from time import sleep
print('Gerador de PA. \n-=-=-=-=-=-=-=-=-=-=')
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
cont = 1
while cont <= 10:
    print('{}'.format(primeiro), end=' -> ')
    primeiro = primeiro + razão
    cont = cont + 1
#print('total de termos utilizados: {}'.format(cont - 1))
for c in range(1, 1000):
    v1 = int(input('Quantos termos você quer mostrar mais?'))
    contv1 = cont + v1
    while cont <= contv1 - 1:
        print(primeiro, end=' -> ')
        primeiro = primeiro + razão
        cont = cont + 1
    if v1 == 0:
        print('total de termos utilizados: {}'.format(cont - 1))
        print('FIM.')
        sleep(1000)'''







'''if cont == contv1:
        print('Mais termos?', end=' ')
        v1 = int(input('Quantos termos você quer?'))'''
'''cliente = input('Quer continuar?Sim ou não:').upper()
if cliente == 'SIM':
    print('ok.')
    v1 = int(input('Quantos termos você quer?'))
    while:
        primeiro = primeiro + razão
        print(primeiro)
        cont = cont + v1
elif cliente == 'NÃO':
    print('FIM.')'''
#print('total de termos utilizados: {}'.format(cont - 1))





