lista = []
for l in range(0, 5):
    lista.append(int(input(f'Digite um um número na posição {l}: ')))
    print(lista)
print(f'O maior valor da lista foi {max(lista)} na posição:', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end=' ')
print(f'\nO menor valor da lista foi {min(lista)} na posição:', end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end=' ')
