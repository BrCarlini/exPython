print('========== CONVERTOR EM DOLARES ==========')
reais = float(input('Digite sua quantia em R$: '))
dolar = float(input('Digite cotação atual: '))
calculo = reais / dolar

print(f'Valor em R$: {reais:.2f}\nCotação: {dolar:.2f}\nValor em US$: {calculo:.2f}')
