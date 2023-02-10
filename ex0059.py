from time import sleep
n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo número:'))
função = 0
while função != 5:
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(1)
    print('O que você pretende fazer com os números {} e {}?'.format(n1, n2))
    print('''-=-=-=-=-=-=-=-=-=-=
    Somar[1]
    Multiplicar[2]
    Maior[3]
    Novos números[4]
    Sair do programa[5]''')
    função = int(input('>>>>> Informe sua opção:'))
    if função == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
        print('-=' * 10)
    elif função == 2:
        print('O produto entre {} e {} é {}'.format(n1, n2, n1 * n2))
        print('-=' * 10)
    elif função == 3:
        if n1 == n2:
            print('Ambos os números são iguais.')
        else:
            if n1 < n2:
                print('Entre {} e {}, o maior é {}'.format(n1, n2, n2))
            else:
                print('Entre {} e {}, o maior é {}'.format(n1, n2, n1))
    elif função == 4:
        print('Ok, digite seus novos valores.')
        n1 =float(input('Primeiro valor:'))
        n2 = float(input('Segundo valor:'))
    elif função > 5 or função < 0:
        print('Opção inválida. Tente novamente.')
print('Fim do programa. Volte sempre!')
