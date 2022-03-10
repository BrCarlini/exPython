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


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')


def titulo(t):
    tam_t = len(t) + 20
    print('-' * tam_t)
    print(f'          {t}')
    print('-' * tam_t)


def resumo(n, aumento=10, reducao=5):
    titulo('RESUMO DO VALOR')
    print(f'Preço analisado: \tR${moeda(n)}')
    print(f'Dobro do preço: \tR${dobro(n)}')
    print(f'Metade do preço: \tR${metade(n)}')
    print(f'{aumento}% de aumento: \tR${aumentar(n, aumento)}')
    print(f'{reducao}% de redução: \tR${diminuir(n, reducao)}')
    print('-'*35)



