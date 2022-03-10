from datetime import datetime
trabalhador = dict()

while True:
    trabalhador['nome'] = str(input('Nome: '))
    trabalhador['idade'] = int(input('Ano de Nascimento: '))
    trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if trabalhador['ctps'] == 0:
        break
    trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    break

ano_atual = datetime.today().year
idade = ano_atual - trabalhador['idade']
trabalhador['idade'] = idade

if trabalhador['ctps'] != 0:
    a = trabalhador['contratacao']
    ultimo_ano = a + 35
    a_nasc = ano_atual - idade
    ano_aposentadoria = ultimo_ano - a_nasc
    trabalhador['aposentadoria'] = ano_aposentadoria

print('-=' * 60)
print(trabalhador)
for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')
