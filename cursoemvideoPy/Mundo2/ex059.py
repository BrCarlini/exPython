print('===================================')
print('============== Menu ===============')
print('===================================')

n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
opcao = 6

while opcao != 5:
    print('''\nEscolha uma das opções:
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos Números
            [5] Sair do Programa''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        somar = n1 + n2
        print(f'{n1} + {n2} = {somar}')

    elif opcao == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O 1° número é maior: {n1:.2f}')
        else:
            print(f'O 2° número é maior: {n2:.2f}')
    elif opcao == 4:
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
    else:
        print('Opção inválida. Tente novamente.')


print('\nPrograma finalizado!')