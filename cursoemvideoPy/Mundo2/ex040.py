print('-=' * 20)
print('            MÉDIA DO ALUNO')
print('-=' * 20)

cor = {'verde': '\033[32m',
       'vermelho': '\033[31m',
       'amarelo': '\033[33m',
       'limpar': '\033[m'}

n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
media = (n1 + n2) / 2


if n1 <= 10.0 and n2 <= 10.0:
    if media >= 7.0:
        print('{}APROVADO !!!{}'.format(cor['verde'], cor['limpar']))
    elif media < 5.0:
        print('{}REPROVADO !!!{}'.format(cor['vermelho'], cor['limpar']))
    else:
        print('{}RECUPERAÇÃO !!!{}'.format(cor['amarelo'], cor['limpar']))
else:
    print('{}NOTA INVÁLIDA !!!{}'.format(cor['vermelho'], cor['limpar']))
