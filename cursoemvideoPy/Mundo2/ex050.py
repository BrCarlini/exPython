soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}° número inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}')


