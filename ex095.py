from time import sleep
jogadores = []
gols = []
jogador = {}
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    resp = input('Quer continuar? [S/N]: ').strip()[0]
    if resp in 'Nn':
        break
print('-='*20)
print(f'cod nome{"gols":^10}{"total":^15}')
cont = -1
for j in jogadores:
    cont += 1
    print(f' {cont} {j["nome"]}    {j["gols"]}{j["total"]:^15}')
while True:
    print('-'*30)
    opção = int(input('Qual jogador quer mostrar? (999 para parar)'))
    if opção == 999:
        break
    print(f'O LEVANTAMENTO DO JOGADOR {jogadores[opção]["nome"]}:')
    for i, g in enumerate(jogadores[opção]['gols']):
        print(f'Na partida {i+1} fez {g} gols')
        sleep(1)
print('PROGRAMA ENCERRADO. Volte sempre!')
