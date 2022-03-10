print('============ TIPO PRIMITIVO & INFOS ============')

check_types = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(check_types)}')
print(f'È alfanumérico ? {check_types.isalnum()}')
print(f'È um número ? {check_types.isnumeric()}')
print(f'È alfabético ? {check_types.isalpha()}')
print(f'Só tem espaços ? {check_types.isspace()}')
