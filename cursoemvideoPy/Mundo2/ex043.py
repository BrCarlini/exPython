print('-=' * 20)
print(' ' * 12, 'CALCULO IMC')
print('-=' * 20)

cor = {'limpar': '\033[m',
       '1': '\033[33m',
       '2': '\033[32m',
       '3': '\033[31m'}

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
calc = peso / altura ** 2

if calc < 18.5:
    print('IMC: {:.1f}\n{}Abaixo do Peso.{}'.format(calc, cor['1'], cor['limpar']))
elif calc <= 25:
    print('IMC: {:.1f}\n{}Peso ideal.{}'.format(calc, cor['2'], cor['limpar']))
elif calc <= 30:
    print('IMC: {:.1f}\n{}Sobrepeso.{}'.format(calc, cor['1'], cor['limpar']))
elif calc <= 40:
    print('IMC: {:.1f}\n{}Obesidade.{}'.format(calc, cor['1'], cor['limpar']))
else:
    print('IMC: {:.1f}\n{}Obesidade Mórbida.{}'.format(calc, cor['3'], cor['limpar']))

