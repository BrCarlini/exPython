from random import randint

numeros = list()

print(f'Sorteando 5 valores da lista: ', end='')


def sorteia():
    for s in range(0, 5):
        s = randint(0, 10)
        numeros.append(s)
        print(f'{s} ', end='')


numeros.append(sorteia())
numeros.pop()
print('PRONTO!')


def soma_par():
    a = 0
    for i in numeros:
        if i % 2 == 0:
            a = a + i
    print(f'Somando os valores pares de {numeros}, temos {a}')


soma_par()
