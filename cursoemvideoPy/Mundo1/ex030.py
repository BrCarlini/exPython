print('========= PAR OU ÍMPAR =========')

n = int(input('Digite um numero inteiro: '))
calc = n % 2

if calc == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')

