while True:
    tabuada = float(input('Digite um número para mostra a sua tabuada:'))
    if tabuada < 0:
        break
    print('-'*20)
    for c in range(1, 11):
        resultado = tabuada * c
        print(f'{tabuada} X {c} = {resultado}')
    print('-'*20)
print('-~'*15)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
