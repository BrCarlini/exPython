


def voto(ano_nasc):
    from datetime import datetime

    ano_atual = datetime.today().year
    idade = ano_atual - ano_nasc
    print(f'Com {idade} anos: ', end='')
    if 18 <= idade < 65:
        return 'VOTO OBRIGATÓRIO.'
    elif idade >= 65:
        return 'VOTO OPCIONAL'
    elif idade < 18:
        return 'NÃO VOTA'


entrada_idade = int(input('Em que ano você nasceu? '))
user = voto(entrada_idade)
print(user)
