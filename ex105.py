def notas(*nota, sit=False):
    """
     -> Função para calcular a maior, menor e média de uma
       turma.
    :param nota: Nota dos alunos
    :param sit: Situação (opcional) da média da turma.
    :return:
    """
    maior = menor = 0
    turma = {}
    turma['total'] = len(nota)
    turma['Maior'] = max(nota)
    turma['Menor'] = min(nota)
    turma['Média'] = sum(nota) / len(nota)
    if sit:
        if 7 > turma['Média'] >= 6:
            turma['Situação'] = 'RAZOÁVEL'
        elif 9 > turma['Média'] > 7.5:
            turma['Situação'] = 'BOA'
        elif turma['Média'] >= 10:
            turma['Situação'] = 'ÓTIMA'
        elif 5.5 > turma['Média']:
            turma['Situação'] = 'RUIM'
    return turma


resp = notas( 5, 10, 7.5, 3.6, sit=True)
print(resp)
help(notas)
