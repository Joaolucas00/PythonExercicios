from time import sleep
print('-'*40)
print(f'{"Manipualador de conjunto":^40}')
print('-' * 40)
while True:
    conj1 = []
    conj2 = []
    comum = []
    while True:
        elemento1 = int(input('Digite um número para a primeira lista: '))
        if elemento1 in conj1:
            print('Elemento repetido...')
        else:
            conj1.append(elemento1)
        continuar1 = str(input('Quer continuar? [S/N]: ').strip()[0])
        if continuar1 in 'Nn':
            print(f'O primeiro conjunto é {conj1}.')
            sleep(3)
            print('-'*30)
            break
    if continuar1 in 'Nn':
        while True:
            elemento2 = int(input('Digite um número para a segunda lista:'))
            if elemento2 in conj2:
                print('Elemento repetido...')
            else:
                conj2.append(elemento2)
            continuar2 = str(input('Quer continuar? [S/N]: ').strip()[0])
            if continuar2 in 'Nn':
                print(f'O segundo conjunto é {conj2}.')
                sleep(3)
                break
    opção = 0
    while opção != 3:
        print(f'\n{"-"*30}\nSomar[1]\nComum[2]\nNovos conjuntos[3]\nEncerrar o programa[4]')
        print('-'*30)
        opção = int(input('O que você quer fazer com os dois conjuntos?'))
        if opção == 1:
            print('~'*40)
            #total = 0
            print(f'A soma do primeiro conjunto {conj1} com a do segundo {conj2} foi:\n {conj1 + conj2}')
            '''for tamanho in range(0, len(conj1 + conj2)):
                total += 1'''
            print(f'O total de elementos foi {len(conj1 + conj2)}.')
            sleep(5.5)
        if opção == 2:
            print('↓'*35)
            for elem in conj1:
                if elem in conj2:
                    comum.append(elem)
            print(f'Os elementos em comum são {comum}.')
            sleep(5)
        if opção == 3:
            print('Ok. Vamos começar de novo.')
            sleep(0.5)
            print('.')
            sleep(0.5)
            print('.')
            sleep(0.5)
            print('.')
            sleep(0.5)
            print('~' * 40)
        if opção == 4:
            print('Encerrando o programa', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.')
            sleep(1.5)
            break
    if opção == 4:
        break
print('Programa encerrado. Volte sempre!')





'''
c = ["c", "b", "a", "p"]
d = ["d", "b", "a", "h"]
#c = ["a", "b", "c"]
#d = ["d", "e", "f"]
e = c + d
cont = 0
print(e)
for f in c and d:
    cont += 1
    if cont == 1:
        print('Os elementos são:', end=', ')
    #print(f, end=' ->  ')
    if f in d and f in c:
        print(f, end=', ')
        {"↓"*40}
'''