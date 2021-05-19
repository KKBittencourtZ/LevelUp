expressão = list()
expressão.append(str(input('Digite uma expressão: ')))
if expressão[0].count('(') == expressão[0].count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
