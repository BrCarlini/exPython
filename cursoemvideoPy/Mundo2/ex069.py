print('-=' * 20)
print('CADASTRE UMA PESSOA')
print('-=' * 20)

c_idade = 0
c_homem = 0
c_mulher = 0
c_mulher_20 =0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('Quer continuar ? [S/N]')
    opcao = str(input('>>> ')).strip().upper()
    # if opcao == 'S':
    if idade > 18 and sexo == 'M':
        c_homem += 1
        c_idade += 1
    elif idade > 18 and sexo == 'F':
        c_mulher += 1
        c_idade += 1
    elif idade <= 18 and sexo == 'M':
        c_homem += 1
    elif sexo == 'F' and idade < 20:
        c_mulher_20 += 1
    if opcao == 'N':
        print('========== FIM DO PROGRAMA ==========')
        print(f'Total de pessoas com mais de 18 anos: {c_idade}.')
        print(f'Ao todo temos {c_homem} homens cadastrados.')
        print(f'E temos {c_mulher_20} mulher(es) com menos de 20 anos.')
        break
