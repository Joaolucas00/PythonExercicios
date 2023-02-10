aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'A méida de {aluno["nome"]}: '))
print('-'*15)
print(f'O nome é {aluno["nome"]}')
print(f'A média é {aluno["média"]}')
if aluno['média'] >= 7:
    print('- A situação é APROVADO.')
elif aluno['média'] < 7:
    print('- A situação é RECUPERAÇÃO.')
elif aluno['média'] < 5:
    print('- A situação é REPROVADO:')
