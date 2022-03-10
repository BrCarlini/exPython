nome = str(input('Digite seu nome completo: ')).strip()
check_name = nome.split()
print(check_name)

print(f'Nome completo: {nome}')
print(f'Primeiro nome: {check_name[0]}')
print(f'Ultimo nome: {check_name[-1]}')

