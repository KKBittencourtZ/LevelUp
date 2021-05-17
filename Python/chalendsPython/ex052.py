cont = 0
x = int(input('Digite um número inteiro: '))
for c in range(1, x + 1):
    if x % c == 0:
        cont += 1
    print(c, end=' ')
print(f'\nO número {x} foi divisível {cont} vezes.')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
