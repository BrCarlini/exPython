print('=========== Análisador de String ===========')

nome_completo = str(input('Digite seu nome completo: ')).strip()

letra_maiuscula = nome_completo.upper()
print(f'Nome em Maiúsculo: {letra_maiuscula}')

letra_minuscula = nome_completo.lower()
print(f'Nome em Minúsculo: {letra_minuscula}')

quantidade_letras = len(nome_completo) - nome_completo.count(' ')
print(f'Quantidade de letras do nome: {quantidade_letras}')

fist_name = nome_completo.split()
print(fist_name)

number_of_letters = len(fist_name[0])
print(f'Quantidade de letras do primeiro nome: {number_of_letters}')

