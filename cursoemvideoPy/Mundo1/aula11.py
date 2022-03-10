"""
ANSI - Escape Sequence
ESTILO, COR EM SEU CÓDIGO

SINTAXE = \033[style:text:back m

Style = 0 none; 1 bold; 4 underline; 7 negative.
Text = 30 branco; 31 vermelho; 32 verde; 33 amarelo; 34 azul; 35 roxo; 36 azul claro; 37 cinza.
Background = 40 branco; 41 vermelho; 42 verde; 43 amarelo; 44 azul; 45 roxo; 46 azul claro; 47 cinza.
"""

print('\033[4:31:40mHello World !!!\033[m')
print('\033[7mHello World !!!\033[m')

cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;31m'}

nome = str(input('Informe seu nome: '))
print('Bem-Vindo, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

