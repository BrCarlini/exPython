print('-=' * 20)
print('COMPARANDO NÚMEROS')
print('-=' * 20)

cor = {'limpar': '\033[m',
       'azul': '\033[34m',
       'amarelo': '\033[33m'}


n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

if n1 > n2:
    print('O {}1°{} número é maior.'.format(cor['amarelo'], cor['limpar']))
elif n2 > n1:
    print('O {}2°{} número é maior.'.format(cor['amarelo'], cor['limpar']))
else:
    print('Não existe valor maior, os dois são {}iguais{}.'.format(cor['azul'], cor['limpar']))
