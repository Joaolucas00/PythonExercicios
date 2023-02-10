jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(1, partidas+1):
    gol = int(input(f'Quantos gols da partida {c}? '))
    gols.append(gol)
    jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*23)
print(jogador)
print('-='*23)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*23)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidads.')
for i, g in enumerate(gols):
    print(f'  => Na partida {i+1}, fez {g}.')
print(f'Foi um total de {jogador["total"]} gols.')
