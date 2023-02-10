def leiaInt(msg=''):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print(f'\033[31mERRO! O erro foi {erro.__class__}. Digite um número inteiro.\033[m')
        else:
            return n


def leiaFloat(msg=''):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except Exception as erro:
            print(f'\033[31mERRO! O erro foi {erro.__class__}. Tente novamente.\033[m')
        else:
            return n

