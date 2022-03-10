print('========== ALUGUEL DE CARROS ==========')
km = float(input('Quantos KM foram percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado: '))
preco_dia = dias * 60
preco_km = km * 0.15

preco_total = preco_dia + preco_km
print(f'TOTAL DE PREÇO A PAGAR R${preco_total:.2f}\nValor em dias: R${preco_dia:.2f}\nValor em Km: R${preco_km}')
