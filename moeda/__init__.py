def metade(núm=0):
    return núm / 2


def dobro(núm=0):
    return núm * 2


def aumento(núm=0, taxa=0):
    res = núm + (núm * taxa / 100)
    return res


def diminuir(núm=0, taxa=0):
    res = núm - (núm * taxa / 100)
    return res


def moeda(núm=0, moeda = 'R$'):
    return f'{moeda}{núm:.2f}'.replace('.', ',')


def resumo(núm=0, taxaA=10, taxaR=5):
    print('-'*30, '\n     RESUMO DO VALOR')
    print('-'*30)
    print(f'O dobro de {moeda(núm)}: \t{moeda(dobro(núm))}')
    print(f'A metade de {moeda(núm)}: \t{moeda(metade(núm))}')
    print(f'{taxaA}% de aumento: \t\t{moeda(aumento(núm, taxaA))}')
    print(f'{taxaR}% de redução: \t\t{moeda(diminuir(núm, taxaR))}')
    print('-'*30)

