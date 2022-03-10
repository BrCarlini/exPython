lista_pessoas = list()
dados_pessoas = dict()

while True:
    dados_pessoas['nome'] = str(input('Nome: ')).title()
    dados_pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper()
    dados_pessoas['idade'] = int(input('Idade: '))
    lista_pessoas.append(dados_pessoas.copy())
    opcao = str(input('Quer continuar ? [S/N] ')).upper()
    if opcao == 'N':
        break
print('-='*30)

print(f'- O grupo tem {len(lista_pessoas)} pessoas.')

# Pega as idades e soma, depois faz uma media de idade
total = 0
media = 0
for d in lista_pessoas:
    total += d['idade']
    media = total / len(lista_pessoas)
print(f'- A média de idade é de {media:.2f}')

# Verifica se a pessoa é do Sexo Feminino, e mostra o nome da pessoa
print(f'- As mulheres cadastradas foram: ', end='')
for dic in lista_pessoas:
    if dic['sexo'] == 'F':
        print(f'{dic["nome"]}; ', end='')

# Pega as pessoas que estão acima da media de idade
print('\n- Lista das pessoas que estão acima da média:')
print()
for i in lista_pessoas:
    if i['idade'] >= media:
        print(f'nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
print('-='*30)

print('<< ENCERRADO >>')
