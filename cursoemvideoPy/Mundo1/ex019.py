import random
print('---------- Sortear Aluno ----------')

aluno1 = input('Informe o aluno 1: ')
aluno2 = input('Informe o aluno 2: ')
aluno3 = input('Informe o aluno 3: ')
aluno4 = input('Informe o aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)
print(f'Dentre os alunos: {alunos}\nO aluno sorteado foi {sorteio}.')
