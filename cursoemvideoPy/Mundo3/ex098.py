from time import sleep


def contador(inicio, fim, passo):
    for n in range(inicio, fim, passo):
        print(f'{n} ', end='')
        sleep(0.5)
    print('FIM!')
    print('-=' * 30)


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)

print('Contagem de 10 até 0 de 2 em 2')
contador(10, -1, -2)

