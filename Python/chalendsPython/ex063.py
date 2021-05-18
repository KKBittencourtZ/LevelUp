print('-' * 26)
print('  Sequência de Fibonacci')
print('-' * 26)
x = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
cont = 2
print('~' * 26)
print(f'{n1} -> {n2} -> ', end='')
while cont != x:
    termo = n1 + n2
    print(termo, end=' -> ')
    n1 = n2
    n2 = termo
    cont += 1
print('FIM')
print('~' * 26)
