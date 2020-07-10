aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
situacao = ''
if aluno['média'] >= 7.0:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print(f'nome é igual a {aluno["nome"]}')
print(f'média é igual a {aluno["média"]}')
print(f'situaçao é igual a {situacao}')