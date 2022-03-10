numeros = list()
mai = 0
men = 0

for cont in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {cont}°: ')))
    if cont == 0:
        mai = men = numeros[cont]
    else:
        if numeros[cont] > mai:
            mai = numeros[cont]
        if numeros[cont] < men:
            men = numeros[cont]
print('=-' * 30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(numeros):
    if v == men:
        print(f'{i}... ', end='')
print()

# print(f'O maior valor digitado foi {max(numeros)} nas posições {numeros.index(max(numeros))}')
# print(f'O menor valor digitdo foi {min(numeros)} nas posições {numeros.index(min(numeros))}')

