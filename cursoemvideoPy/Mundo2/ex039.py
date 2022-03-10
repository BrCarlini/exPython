
from datetime import date

print('-=' * 20)
print('SERVIÇO MILITAR')
print('-=' * 20)

ano_nasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Informe sua sexualidade:\n[M] para Masculino.\n[F]para Feminino.\n>>>')).upper()
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if sexo == 'M':
    if idade == 18:
        print('Este ano você deverá se alistar!')
    elif idade < 18:
        prazo = 18 - idade
        print(f'Você ainda NÃO tem 18 anos. Faltam {prazo} ano(s) para se alistar.')
        ano = ano_atual + prazo
        print(f'Seu alistamento será em {ano}.')
    elif idade > 18:
        prazo = idade - 18
        print(f'Você já deveria ter se alistado há {prazo} ano(s).')
        ano = ano_atual - prazo
        print(f'Seu alistamento foi em {ano}.')
else:
    print('Não precisa se alistar.')
