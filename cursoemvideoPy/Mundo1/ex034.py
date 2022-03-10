print('============ AUMENTO SALARIAL ============')

salario = float(input('Informe seu salário: '))
aumento = 0


if salario > 1250.00:
    aumento = salario * 10 / 100
    print(f'Seu aumento foi de 10%: R${aumento}\nSeu salário total ficou de R${salario + aumento}.')
else:
    aumento = salario * 15 / 100
    print(f'Seu aumento foi de 15%: R${aumento}\nSeu salário total ficou de R${salario + aumento}.')

print('Parabens!!!')
