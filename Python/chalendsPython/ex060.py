numero = int(input('Digite um número para calcular seu Farorial: '))
fat = 1
print(f'Calculando {numero}! =', end=' ')
for c in range(numero, 0, -1):
    fat *= c
    if c == 1:
        print(f'{c}', end=' = ')
    else:
        print(f'{c}', end=' x ')
print(fat)
# OBS: Dá para fazer usando o while
