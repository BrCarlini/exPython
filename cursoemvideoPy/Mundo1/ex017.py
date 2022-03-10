print('======= Calculo Hipotenusa =======')
from math import hypot

cat_oposto = float(input('Digite o Cateto Oposto: '))
cat_adjacente = float(input('Digite o Cateto Adjacente: '))
calc_hipotenusa = hypot(cat_oposto, cat_adjacente)

print(f'Cateto Oposto: {cat_oposto}\nCateto Adjacente: {cat_adjacente}\nHipotenusa: {calc_hipotenusa:.2f}')
