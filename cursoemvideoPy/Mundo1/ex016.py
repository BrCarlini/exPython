print('====== UTILIZANDO :.0f ======')
n1 = float(input('Digite um número: '))
print(f'Utilizando a formatação direto no print:  {n1:.0f}')

print('=========================================================')

from math import trunc


print('====== UTILIZANDO from math import trunc ======')
n2 = float(input('Digite outro número: '))
inteiro = trunc(n2)
print(f'Utilizando a importação de math: {inteiro}')


print('Conclusão: utilizando a formatação o numero informado é arredondado.\nUtilizando a importação de math e trunc o numero é apresentado apenas a sua parte inteira.')

