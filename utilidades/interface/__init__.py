def line(l='-', tam=20):
    print(l*tam)


def menu(msg=''):
    line('-', 40)
    print(msg.center(40))
    line('-', 40)


def opção(lista):
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
