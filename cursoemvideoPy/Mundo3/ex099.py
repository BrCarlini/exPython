from time import sleep


def maior(* num):
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('-='*30)


maior(7, 8, 9, 10)
maior(2, 4)
maior(1, 2, 3)
maior(0)
maior()  # Ocorrendo erro de ValueError por conta da função max()
maior(3, 5, 7, 8, 0, 1, 9, 19)

