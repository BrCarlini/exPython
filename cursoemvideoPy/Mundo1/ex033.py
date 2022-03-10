n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

numeros = [n1, n2, n3]
maior = max(numeros)
menor = min(numeros)

if maior == n1:
    print(f'O 1° número é o maior: {maior}')
elif maior == n2:
    print(f'O 2° número é o maior: {maior}')
elif maior == n3:
    print(f'O 3° número é o maior: {maior}')
else:
    print('-------------------------------')

if menor == n1:
    print(f'O 1° número é o menor: {menor}')
elif menor == n2:
    print(f'O 2° número é o menor: {menor}')
elif menor == n3:
    print(f'O 3° número é o menor: {menor}')
else:
    print('-------------------------------')