from random import randint
print('===================================')
print('======= JOGO DA ADIVINHAÇÃO =======')
print('===================================')




aleat = randint(0, 5)
n = int(input('Digite um número: '))

if n == aleat:
    print('Você acertou!! Miseravi')
else:
    print('Errou!! Teste mais tarde.')

print(f'Número pensado pela máquina: {aleat}')
