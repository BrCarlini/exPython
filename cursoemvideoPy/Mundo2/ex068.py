from random import randint

print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)

n = 0
c = 0

while True:
    n = int(input('Digite um número: '))
    aleat = randint(0, 10)
    opcao = str(input('Par ou Ímpar [P/I] ? ')).upper()
    calc = n + aleat
    # print(f'Você jogou {n} e o computador {aleat}.')

    if opcao == 'P' or opcao == 'I':
        if opcao == 'P':
            if calc % 2 == 0 and opcao == 'P':
                print('Total de {}, DEU PAR.'.format(calc, end=''))
                c += 1
                print('Você VENCEU\n')
                print('Vamos jogar novamente...')
                print('-\n' * 3)
            else:
                print(f'Total de {calc}, DEU ÍMPAR')
                print('Você PERDEU\n')
                print('-=' * 30)
                print(f'GAME OVER! Você venceu {c} vezes')
                break
        else:
            if opcao == 'I':
                if calc % 2 == 1:
                    print(f'Você jogou {n} e o computador {aleat}. Total de {calc}, DEU ÍMPAR.')
                    c += 1
                    print('Você VENCEU\n')
                    print('Vamos jogar novamente...')
                    print('-\n' * 3)
                else:
                    print(f'Você jogou {n} e o computador {aleat}. Total de {calc}, DEU PAR.')
                    print('Você PERDEU\n')
                    print('-=' * 30)
                    print(f'GAME OVER! Você venceu {c} vezes')
                    break
    else:
        print('Opção Inválida.')
        break

