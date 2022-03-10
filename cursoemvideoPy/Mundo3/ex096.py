def area(larg, compri):
    calc = larg * compri
    print(f'A área de um terreno {larg}x{compri} é de {calc}m².')


print(f'     CONTROLE DE TERRENOS')
print('-'*30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)

