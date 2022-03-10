lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('=========================')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=========================')
print('Comi pra caramba.')
print('=========================')

a = (2, 5, 4)
b = (5, 8, 1, 2, 8)
c = b + a
print(c)
print(f'Quantos elementos tem na tupla? {len(c)}')
print(f'Quantos 5 tem na tupla? {c.count(5)}')
print(f'Em que posição esta o 8? {c.index(8)}')