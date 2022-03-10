times = ('AtleticoMG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'AmericaMG', 'AtleticoGO', 'Santos', 'Ceara',
         'Internacional', 'São Paulo', 'AthleticoPR', 'Cuiaba', 'Juventude', 'Gremio',
         'Bahia', 'Sport', 'Chapecoense')
print(f'-> Lista de Times do Brasileirão: {times}\n')
print(f'-> Os cinco primeiros colocados são: {times[:5]}\n')
print(f'-> Os 4 últimos são: {times[-4:]}\n')
print(f'-> Times em ordem alfabética: {sorted(times)}\n')

for p, t in enumerate(times):
    p += 1
    # print(f'{t} -> {p}')
    if 'Chapecoense' in t:
        print(f'-> A Chapecoense está na {p}° posição')
