
n = int(input('Digite um número: '))
c = 1
print(f'------- TABUADA DO {n} -------')
for i in range(1, 11):
    mult = n * i
    print(f'{n} x {c} = {mult}')
    c += 1

