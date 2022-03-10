brasil = []  # Lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # Dicionario
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  # Dicionario
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print()
print(brasil[0])
print(brasil[1])
print()
print(brasil[0]['uf'])
print(brasil[1]['uf'])
print('-='*30)
print()

city = dict()
brazil = list()

for c in range(0, 3):  # Pegar dados
    city['uf'] = str(input('Unidade Federativa: '))
    city['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(city.copy())
print(brazil)
print()

for c in brazil:  # Pega os valores(dict) da lista Brazil
    print(c)
print()

for e in brazil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

