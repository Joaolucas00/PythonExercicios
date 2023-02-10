tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezesseis',
         'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um número de 0 a 20:').strip())
    if 0 <= num <= 20:
        break
    else:
        print('Tente novamente.', end=' ')
print(f'O número que você digitou foi {tupla[num]}.')
