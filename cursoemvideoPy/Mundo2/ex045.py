from random import choice
from time import sleep

print('-=' * 20)
print(' ' * 11, 'GAME JOKENPÔ')
print('-=' * 20)
estilo = '/' * 50
cor = {'limpar': '\033[m',
       'red': '\033[31m',
       'green': '\033[32m',
       'yellow': '\033[33m',
       'white': '\033[7:40m'}

print('{}{}{}'.format(cor['white'], estilo, cor['limpar']))

player = str(input('Informe uma das opções:\n-> Pedra\n-> Papel\n-> Tesoura\n>>> ')).lower().strip()
print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
lista_op = ['pedra', 'papel', 'tesoura']
maquina = choice(lista_op)
print(' ')


if player == 'pedra' and maquina == 'pedra':
    print(f'A Maquina escolheu: {maquina}')
    print('{}Empate.{}'.format(cor['yellow'], cor['limpar']))
elif player == 'pedra' and maquina == 'papel':
    print(f'A Maquina escolheu: {maquina}')
    print('{}MAQUINA VENCEU.{}'.format(cor['red'], cor['limpar']))
elif player == 'pedra' and maquina == 'tesoura':
    print(f'A Maquina escolheu: {maquina}')
    print('{}VOCÊ VENCEU.{}'.format(cor['green'], cor['limpar']))
elif player == 'papel' and maquina == 'papel':
    print(f'A Maquina escolheu: {maquina}')
    print('{}Empate.{}'.format(cor['yellow'], cor['limpar']))
elif player == 'papel' and maquina == 'pedra':
    print(f'A Maquina escolheu: {maquina}')
    print('{}VOCÊ VENCEU.{}'.format(cor['green'], cor['limpar']))
elif player == 'papel' and maquina == 'tesoura':
    print(f'A Maquina escolheu: {maquina}')
    print('{}MAQUINA VENCEU.{}'.format(cor['red'], cor['limpar']))
elif player == 'tesoura' and maquina == 'tesoura':
    print(f'A Maquina escolheu: {maquina}')
    print('{}Empate.{}'.format(cor['yellow'], cor['limpar']))
elif player == 'tesoura' and maquina == 'pedra':
    print(f'A Maquina escolheu: {maquina}')
    print('{}MAQUINA VENCEU.{}'.format(cor['red'], cor['limpar']))
elif player == 'tesoura' and maquina == 'papel':
    print(f'A Maquina escolheu: {maquina}')
    print('{}VOCÊ VENCEU.{}'.format(cor['green'], cor['limpar']))
else:
    print('{}VALOR INVÁLIDO!{}'.format(cor['red'], cor['limpar']))


print(' ')
print('{}{}{}'.format(cor['white'], estilo, cor['limpar']))
