from time import sleep
alunos = []
aluno = []
notas = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    aluno.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    notas.append(média)
    aluno.append(notas[:])
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    #print(alunos)
    continuar = str(input('Quer continuar? [S/N]: ').strip()[0])
    if continuar in 'Nn':
        break
print('-='*25)
print('No.', f'{"NOME":^10}{"MÉDIA":^10}')
print('-'*30)
for a in range(0, len(alunos)):
    print(a, f'{alunos[a][0]:^10}', f'{alunos[a][1][2]:^10}')
print('-'*30)
alunoNota = 0
while True:
    alunoNota = int(input('Quer mostrar a nota de qual aluno? (999 interrompe): '))
    if alunoNota == 999:
        break
    print(f'A nota de {alunos[alunoNota][0]} são {alunos[alunoNota][1][0]} e {alunos[alunoNota][1][1]}')
    print('-'*30)
print('ENCERRANDO O PROGRAMA', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(1)
