numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar ? [S/N] ')).upper()
    if opcao != 'S':
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Lista completa: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')

