def leia_int(msg):
    """

    :param msg: Recebe um input de tipo Str
    :return: Converte o parametro(str) para Int
    """
    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
