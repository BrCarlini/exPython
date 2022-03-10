tab = int(input('Informe a tabuada que deseja calcular: '))

for n in range(1, 11):
    calc = tab * n
    print(f'{tab} x {n} = {calc}')

