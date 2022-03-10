from datetime import date

print('-=' * 5)
print('CATEGORIA\n  de\nNATAÇÃO')
print('-=' * 5)
print(' ')

ano_nasc = int(input('Digite sua data de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} ano(s).')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: MASTER')