print('========== Passagem de Onibus ==========')

km = float(input('Informe o Km da sua viagem: '))

if km <= 200.0:
    preco = km * 0.50
    print(f'A kilometragem de sua viagem será {km}km e o preço dela será de R${preco:.2f}.')
else:
    preco = km * 0.45
    print(f'A kilometragem de sua viagem será {km}km e o preço dela será de R${preco:.2f}!!')


print('========== Boa Viagem ==========')

