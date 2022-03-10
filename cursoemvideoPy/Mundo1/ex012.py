print('========= Desconto =========')
preco = float(input('Digite o preço do produto: R$'))
calc = preco - ((5 / 100) * preco)
print(f'Preço digitado R${preco}\nDesconto: 5%\nPreço com desconto: R${calc}')