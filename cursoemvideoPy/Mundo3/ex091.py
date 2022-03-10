from random import randint
from time import sleep

jogadores = {}
for c in range(1, 5):
    jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
                 'jogador4': randint(1, 6)}
print('-='*30)
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'- O {k} tirou {v} no dado.')
    sleep(1)
print('-='*30)

