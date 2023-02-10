def leiaInt(frase=''):
    """
     -> Função para verificar se um número é inteiro positivo.
     Ele tem uma variável "núm" para verificar se é ou não um
     inteiro positivo.
    :param frase: Frase do usuário
    :return: Retorna núm
    """
    while True:
        núm = str(input(frase))
        if núm.isnumeric():
            return núm
        else:
            print('ERRO! Digite um número inteiro positivo válido.')


#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
help(leiaInt)
