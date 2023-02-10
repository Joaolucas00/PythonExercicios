from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram {sorted(tupla)}')
#print(f'O maior valor sorteado foi {sorted(tupla)[-1]}\nO menor valor sorteado foi {sorted(tupla)[0]}')
print(f'O maior valor foi {max(tupla)}\nO menor valor foi {min(tupla)}')
