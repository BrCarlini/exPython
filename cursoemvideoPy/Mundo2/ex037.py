print('-=' * 20)
print('PROGRAMA DE CONVERSÃO DECIMAL')
print('-=' * 20)

n = int(input('Digite um número: '))
base = str(input('Digite a base de conversão: [1]binario; [2]octal; [3]hexadecimal: '))


if base == '1':
    binario = bin(n)
    print('Inteiro: {}\n\033[33mConvertido em binário: {}\033[m'.format(n, binario[2:]))
elif base == '2':
    octal = oct(n)
    print('Inteiro: {}\n\033[33mConvertido em octal: {}\033[m'.format(n, octal[2:]))
elif base == '3':
    hexa = hex(n)
    print('Inteiro: {}\n\033[33mConvertido em hexadecimal: {}\033[m'.format(n, hexa[2:]))
else:
    print('\033[31mOpção Inválida !!!\033[m')


