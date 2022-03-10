print('=' * 25)
print('EMPRÉSTIMO BANCÁRIO')
print('=' * 25)
print(' ')

cor = {'limpar': '\033[m',
       'red': '\033[31m',
       'yellow': '\033[33m',
       'green': '\033[32m',
       'pretoebranco': '\033[7:40m',
       'back_yellow': '\033[30:41m'}

print('{}REGRA:{}\n{}PARCELA NÃO PODE EXCEDER 30% DO SALÁRIO !!!{}'.format(cor['pretoebranco'], cor['limpar'], cor['back_yellow'], cor['limpar']))
print(' ')


valor_casa = float(input('Digite o preço da casa: '))
salario = float(input('Digite seu salário: '))
anos = float(input('Digite a quantidade de anos que gostaria de pagar a casa: '))

parcela = valor_casa / (anos * 12)
regra = salario * 30 / 100

if parcela >= regra:
    print('{}EMPRÉSTIMO NEGADO.{}\n{}Parcela excedeu 30% do Salário.{}'.format(cor['red'], cor['limpar'], cor['yellow'], cor['limpar']))
else:
    print('{}EMPRÉSTIMO APROVADO !!!{}\n{}Valor da parcela: {:.2f}{}'.format(cor['green'],cor['limpar'], cor['yellow'], parcela, cor['limpar']))

print(f'Salário: R${salario}\n30% do seu salário é: R${regra}\nParcela: R${parcela:.2f}')

