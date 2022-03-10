nome = str(input('Qual é seu nome ? '))
if nome == 'Bruno':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Silva':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Alessandra':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')