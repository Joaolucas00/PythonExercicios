from utilidades import interface
def arquivoExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def leiaArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo!')
    else:
        interface.menu('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            print('Nome:', f'{"Idade:":>20}')
            print(f'{dado[0]}{dado[1]:>20}')
        #print(a.readlines())


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro!')
    else:
        a.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome}, idade {idade}')
        a.close()
