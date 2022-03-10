print('-=' * 20)
print('LOJA BARATÃO')
print('-=' * 20)

total_gasto = 0
mais_de_mil = 0
produto_barato = 0
contador = 0

while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    print('Quer continuar ? [S/N]')
    opcao = str(input('>>> ')).strip().upper()

    total_gasto = preco + total_gasto
    contador += 1
    if preco > 1000:
        mais_de_mil += 1
    if contador == 1:
        produto_barato = preco
    else:
        if produto_barato < preco:
            produto_barato = preco
    if opcao == 'N':
        print(f'O total da compra foi R${total_gasto}')
        print(f'Temos {mais_de_mil} produtos custando mais de R$1000')
        print(f'O produto mais barato foi {nome}, que custa {produto_barato}')
        break



