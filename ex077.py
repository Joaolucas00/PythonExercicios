tupla = ('Vogal', 'Tupla', 'Futuro', 'Mercado', 'Loja')
for t in tupla:
    print(f'\na palavra {t} temos ', end='')
    for letra in t:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
