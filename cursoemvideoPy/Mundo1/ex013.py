print('============== AUMENTO SALARIAL ==============')
salario = float(input('Digite seu salário: R$'))
calc = salario + ((15 / 100) * salario)

print(f'Salário digitado: R${salario:.2f}\nSalário com o aumento de 15%: R${calc:.2f}')