while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-' * 40)
    if n >= 0:
        for i in range(1, 11):
            tabuada = n * i
            print(f'{n} x {i} = {tabuada}')
        print('-' * 40)
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')