s = 0
c = 0
while True:
    n = int(input('Digite uma valor [999 para sair]: '))
    if n == 999:
        break
    c += 1
    s = s + n
print(f'A soma dos {c} valores foi {s}')
