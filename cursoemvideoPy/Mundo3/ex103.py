def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome_jogador = str(input('Nome do Jogador: '))
num_gols = str(input('Número de Gols: '))


dado = ficha
print(dado(nome_jogador, num_gols))
