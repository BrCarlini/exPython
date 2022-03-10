import random
print('---------- Sortear Aluno 2 ----------')

aluno1 = input('Informe o aluno 1: ')
aluno2 = input('Informe o aluno 2: ')
aluno3 = input('Informe o aluno 3: ')
aluno4 = input('Informe o aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
print(alunos)

random.shuffle(alunos)
print(f'Ordem de apresentação: {alunos}')
