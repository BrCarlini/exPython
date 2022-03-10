from time import sleep


def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor infromado foi {maior}')


maior(7, 8, 9, 10)
maior(2, 4)
maior(1, 2, 3)
maior(0)
maior()
maior(3, 5, 7, 8, 0, 1, 9, 19)
