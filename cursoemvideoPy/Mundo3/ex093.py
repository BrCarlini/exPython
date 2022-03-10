aprov_jogador = {}
gols = list()
total_gols = 0

aprov_jogador['nome'] = str(input('Nome do Jogador: ')).strip()
aprov_jogador['partidas'] = int(input(f'Quantas partidas {aprov_jogador["nome"]} jogou: '))
num_partidas = aprov_jogador['partidas']


# Pegando cada gol feito nas partidas definidas pelo Usuario
for p in range(1, num_partidas + 1):
    gols.append(int(input(f'Quantos gols na {p}° partida ? ')))
aprov_jogador['gols'] = gols.copy()


# Somando total de Gols
for e in gols:
    total_gols += e
aprov_jogador['total'] = total_gols

print('-='*50)
print(aprov_jogador)
print('-='*50)

# Verificado Chave e Valor de todos os elementos/itens do Dicionario
for k, v in aprov_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)

print(f'O jogador {aprov_jogador["nome"]} jogou {aprov_jogador["partidas"]} partidas.')

# Mostra o valor de gols para cada partida
cont = 0
for part in range(1, aprov_jogador['partidas'] + 1):
    print(f'   => Na partida {part}, fez {aprov_jogador["gols"][cont]} gols')
    cont += 1
print(f'Foi um total de {aprov_jogador["total"]} gols.')

