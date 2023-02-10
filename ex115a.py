from utilidades import interface, numeros
from time import sleep
while True:
    sleep(1.5)
    interface.menu('MENU PRINCIPAL')
    interface.opção(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do programa'])
    interface.line('-', 40)
    while True:
        opç = numeros.leiaInt('Opção: ')
        if opç > 3 or opç <= 0:
            continue
        else:
            break
    if opç == 1:
        interface.menu('Pessoas cadastradas')
    if opç == 2:
        interface.menu('Cadastros de pessoas')
    if opç == 3:
        print('\nPROGRAMA ENCERRADO.\nVolte sempre!')
        break
