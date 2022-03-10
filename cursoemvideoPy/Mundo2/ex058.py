from random import randint
print('{}==================================='.format('\033[33m'))
print('======= JOGO DA ADIVINHAÇÃO =======')
print('==================================={}\n'.format('\033[m'))
print('\033[31mAVISO:\033[m DIGITE NÚMEROS ENTRE 0 E 10\n')

aleat = randint(0, 10)

n = int(input('Digite um número: '))
c = 0

while n != aleat:
    n = int(input('Digite um número: '))
    c += 1
    if n == aleat:
        c += 1
        print('\033[32mAcertou, Miseravi.\033[m')
    else:
        if n < aleat:
            print('Mais... Tente mais uma vez.')
        elif n > aleat:
            print('Menos... Tente mais uma vez.')

print(f'Número de tentativas: {c}')
print(f'Número pensado pela máquina: {aleat}')

