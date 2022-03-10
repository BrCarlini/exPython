numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))

    while n < 0 or n > 20:
        n = int(input('Opção inválida. Digite um número entre 0 e 20: '))

    for i in numero:
        print(f'Você digitou o número {numero[n]}')
        break
    break
print('FIM')

