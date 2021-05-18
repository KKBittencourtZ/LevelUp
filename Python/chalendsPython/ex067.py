while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if valor < 0:
        break    
    for c in range(1, 11):
        print(f'{valor} x {c:2} = {c * valor}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre !')
