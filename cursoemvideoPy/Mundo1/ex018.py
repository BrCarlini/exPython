from math import cos, sin, tan, radians

print('======= Calcular o Seno, Cosseno, Tangente do ângulo. =======')
angulo = int(input('Informe o ângulo: '))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
sen = sin(radians(angulo))

print('----------------------------------')

print(f'O ângulo informado foi {angulo}')
print(f'Seno: {sen:.2f}\nTangente: {tang:.2f}\nCosseno: {coss:.2f}')
