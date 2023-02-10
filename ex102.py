def fatorial(a, show=False):
    """
    Função que calcula fatorial.
    :param a: fatorial de a.
    :param show: mostrar a conta.
    :return: retorna o resultado do fatorial.
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end=' ')
            if c == 1:
                print('=', end=' ')
            else:
                print('x', end=' ')
    return f


print(fatorial(5, True))
