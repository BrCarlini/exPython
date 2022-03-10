frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[letra]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

