from utilidades import interface, numeros, arquivo
from time import sleep
arq = 'Cadastros'
if not arquivo.arquivoExist(arq):
    arquivo.criaArquivo(arq)
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
        arquivo.leiaArquivo(arq)
    if opç == 2:
        interface.menu('Novo cadastro')
        nome = input('Nome: ')
        idade = numeros.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    if opç == 3:
        print('\nPROGRAMA ENCERRADO.\nVolte sempre!')
        break
