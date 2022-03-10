
condicao = str(input('Deseja iniciar programa [S/N]? ')).upper()
ac = 0
contador = 0
media = 0
maior = menor = 0

while condicao != 'N':
    if condicao == 'S':
        n = int(input('Digite um número inteiro: '))
        ac = ac + n
        contador = contador + 1
        media = ac / contador
        condicao = str(input('Deseja continuar [S/N]? ')).upper()
        if contador == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

    else:
        condicao = str(input('Deseja continuar [S/N]? ')).upper()


print(f'Foram lidos {contador} números. A soma entre eles é de {ac}. A média é {media:.2f}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
