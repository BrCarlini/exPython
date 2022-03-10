def metade(n):
    resultado = n / 2
    return resultado


def dobro(n):
    resultado = n * 2
    return resultado


def aumentar(n, porc):
    calc = (n * porc) / 100
    resultado = n + calc
    return resultado


def diminuir(n, porc):
    calc = (n * porc) / 100
    resultado = n - calc
    return resultado


def titulo(t):
    tam_t = len(t) + 10
    print('-' * tam_t)
    print(f'     {t}')
    print('-' * tam_t)


def resumo(n, aumento, reducao):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: R${n}')
    print(f'Dobro do preço: R${dobro(n)}')
    print(f'Metade do preço: R${metade(n)}')
    print(f'{aumento}% de aumento: R${aumentar(n, aumento)}')
    print(f'{reducao}% de redução: R${diminuir(n, reducao)}')



