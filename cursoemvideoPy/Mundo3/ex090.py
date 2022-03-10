aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]:.1f}')

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Situação é igual a {aluno["situacao"]}')
print(aluno)
print()
print('-='*30)
print('Com "enumerate" do Dicionario:')

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
