def metade(n, form=False):
    resultado = n / 2
    return resultado if form is False else moeda(resultado)


def dobro(n, form=False):
    resultado = n * 2
    return resultado if form is False else moeda(resultado)


def aumentar(n, porc, form=False):
    calc = (n * porc) / 100
    resultado = n + calc
    return resultado if form is False else moeda(resultado)


def diminuir(n, porc, form=False):
    calc = (n * porc) / 100
    resultado = n - calc
    return resultado if form is False else moeda(resultado)


def moeda(preco=0, simbolo='R$'):
    return f'{simbolo}{preco:>.2f}'.replace('.', ',')


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
