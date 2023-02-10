def ficha(n='<desconhecido>', g=0):
    """
     -> Função para verificar o Nome e Gols de um Jogador qualquer
    :param n: Nome do Jogador.
    :param g: Gols do jogador.
    :return: Não tem retorno.
    """
    print('-'*20)
    print(f'O {n} fez {g} gol(s) no campeonato.')


#Programa principal
nome = input('Nome do jogador(a): ')
gols = input(f'Gols de {nome}: ')
if gols.isnumeric() and nome.strip() == '':
    ficha(g=gols)
elif gols.isnumeric() == False and nome.strip() != '':
    ficha(n=nome)
elif gols.isnumeric() and nome.strip() != '':
    ficha(n=nome, g=gols)
else:
    ficha()
