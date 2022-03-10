# Fatiamento

frase = 'Curso em Video Python'
        #0123456789
teste = frase[9]
teste2 = frase[9:13]
teste3 = frase[9:21]
teste4 = frase[9:21:2]  # Do 9 até 21 pulando de dois em dois
teste5 = frase[:5]  # Do inicio até o 5
teste6 = frase[15:]  # Do 15 até o final
teste7 = frase[9::3]  # Do 9 pulando de 3 em 3 até o final

print(frase)
print('==============================================')

# Análise

comprimento = len(frase) # Mostra o total do comprimento da string
contador = frase.count('o')  # Conta quantos elementos tem
achar = frase.find('deo')  # Função de achar/encontrar o que é passado como parametro
check = 'Curso' in frase

print(comprimento)
print(contador)
print(achar)
print(check)
print('===============================================')

# Transformação

frase.replace('Python', 'Android')  # Trocar, Substituir
frase.upper()  # Colocar as letras maiuscula
frase.lower()  # Coloca as letras minusculas
frase.capitalize()  # Colocar a primeira letra em maiuscula e o restante minuscula
frase.title()  # Colocar a primeira letra como maiuscula como se fosse titulo
frase.strip()  # Remove os espaços inuteis de uma strig
frase.rstrip()  # Remove os espaços a direita
frase.lstrip()  # Remove os espaços a esquerda
frase.split()  # divide string , gerando uma lista
'-'.join(frase)