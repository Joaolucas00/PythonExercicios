from time import sleep


def mensagem(msg):
    print('-='*20)
    print(f' {msg}')


def contador(início, fim, passo):
    if fim > início:
        for c in range(início, fim+1, passo):
            sleep(0.3)
            print(c, end=' ')
        sleep(0.3)
        print('FIM!')
    elif fim < início:
        if passo > 0:
            for c in range(início, fim-1, passo*-1):
                sleep(0.3)
                print(c, end=' ')
            sleep(0.3)
            print('FIM!')
        else:
            for c in range(início, fim-1, passo):
                sleep(0.3)
                print(c, end=' ')
            sleep(0.3)
            print('FIM!')


mensagem('Contagem de 1 até 10 de 1 em 1')
contador(início=1, fim=10, passo=1)
mensagem('Contagem de 10 até 0 de 2 em 2')
contador(início=10, fim=0, passo=-2)
print('Agora é a sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
mensagem(f'Contando de {início} até {fim} de {passo} em {passo}')
contador(início, fim, passo)
