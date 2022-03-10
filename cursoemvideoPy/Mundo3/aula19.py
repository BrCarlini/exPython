# Dicionarios são compostos por chaves e valores
# dict()

pessoas = {'nome': 'Bruno',
           'sexo': 'M',
           'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())  # Retorna as chaves
print(pessoas.values())   # Retorna os valores
print(pessoas.items())  # Retorna as chaves e os valores
print()

for v in pessoas.values():  # Retorna os valores
    print(f'Valor(values): {v}')

for k in pessoas.keys():  # Retorna as chaves
    print(f'Chaves(keys): {k}')
print()
for k, v in pessoas.items():  # Retorna as keys e values
    print(f'Keys: {k}\nValues: {v}')
print()

# Para apagar
del pessoas['sexo']  # Deleta a chave
pessoas['nome'] = 'Alessandra'  # Altera o valor
pessoas['peso'] = 47  # Adiciona a chave peso atribuindo um valor
print(pessoas.items())

