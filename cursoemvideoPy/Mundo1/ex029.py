print('======= MULTA =======')

km = float(input('Kilometragem obtido no radar: '))

if km > 80.0:
    multa = (km - 80) * 7
    print(f'Você levou uma multa por velocidade.\nSua velocidade: {km:.1f}\nValor da multa: R${multa:.2f}')
else:
    print('Não levou multa.')

