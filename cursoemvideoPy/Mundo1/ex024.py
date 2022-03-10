cidade = input('Digite uma cidade: ').strip()
fatiamento = cidade.split()
check = fatiamento[0].upper()

if check == 'SANTO':
    print('Começa com Santo !!')
else:
    print('Não começa com Santo !!')

#  Ouuuu

print(f"Começa com Santo: {cidade[:5].upper() == 'SANTO'}")
