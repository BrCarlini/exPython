sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor Errado. Digite seu sexo novamente[M/F]: ')).upper().strip()

print(f'Sexo {sexo} inserido com sucesso.')
