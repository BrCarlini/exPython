pessoas = list()
dados = list()
peso = list()

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    opcao = str(input('Deseja continuar ? [S/N] ')).upper().strip()
    print('-='*30)
    if opcao != 'S':
        break


print(pessoas)
# print(peso)
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == max(peso):
        print(p[0], end='; ')

print('\n')

print(f'O menor peso foi de {min(peso):.2f}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == min(peso):
        print(p[0], end='; ')


