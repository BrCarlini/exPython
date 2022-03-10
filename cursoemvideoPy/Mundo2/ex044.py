print('-=' * 20)
print('{:^40}'.format('SISTEMA DE PAGAMENTO'))
print('-=' * 20)

produto = float(input('Digite o preço do produto: '))
forma_pagamento = str(input('Informe o método de pagamento:\n[1]Dinheiro/Cheque\n'
                            '[2]Á vista no cartão de crédito\n[3]Até 2x no crédito\n[4]3x ou mais no crédito\n >>> '))

preco_atual = 0


if forma_pagamento == '1':
    preco_atual = produto - (produto * 10 / 100)
    print(f'Preço com desconto pagando no dinheiro/cheque: {preco_atual}')
elif forma_pagamento == '2':
    preco_atual = produto - (produto * 5 / 100)
    print(f'Preço com desconto pagando á vista no cartão de crédito: {preco_atual}')
elif forma_pagamento == '3':
    print(f'Preço sem desconto parcelando em até 2x no cartão: {produto}')
elif forma_pagamento == '4':
    preco_atual = produto + (produto * 20 / 100)
    print(f'Preço com juros de 20%: {preco_atual}')
else:
    print('Opção Inválida')

