def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    calc = 1

    for i in range(n, 1, -1):
        calc = calc * i
    if show is True:
        for num in range(n, 1, -1):
            print(f'{num} x', end=' ')
        print('1 = ', end='')
    return calc


print(fatorial(6, True))
print(fatorial(5, False))
