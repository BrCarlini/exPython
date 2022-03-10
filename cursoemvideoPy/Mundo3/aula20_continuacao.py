"""
Aula - 20
- Interactive Help
- docstrings
- Argumentos/ Parametros opcionais
- Escopo de variáveis
- Retorno de resultados

"""
# Interactive Help

# help(print)
# help(int)
# print(input.__doc__)
######################################################


# Docstrings


def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passos da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c = c + p
    print('FIM!')


contador(1, 10, 1)
######################################################


# Argumentos/ Parametros opcionais


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(3, 2)
somar()

######################################################


# Escopo de Variáveis(Local ou Global)


def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()
# print(f'No programa principal, x vale {x}')  -> NameError: Não definido, x criado localmente na função

######################################################


# Retorno de resultados


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


resp1 = soma(3, 2, 5)
resp2 = soma(1, 7)
resp3 = soma(4)
print(f'Meus cálculos deram {resp1}, {resp2}, {resp3}.')

