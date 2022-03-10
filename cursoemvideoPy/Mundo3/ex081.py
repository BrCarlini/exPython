numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar ? [S/N] ')).upper()
    if opcao != 'S':
        break

print('-=' * 30)

if 5 in numeros:
    print('O número 5 esta na lista')
else:
    print('O número 5 não está na lista.')

print(f'Lista: {numeros}')
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} numeros')
print(f'Ordenada de forma decrescente: {numeros}')
