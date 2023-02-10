f = int(input('Digite um número para saber seu fatorial:'))
r = 1
for c in range(1, f + 1):
    print('{}'.format(c), end=' ')
    if c >= 1 and c != f:
        print('x', end=' ')
    else:
        print('=', end=' ')
    r = c * r
print('{}! = {}'.format(f, r))
