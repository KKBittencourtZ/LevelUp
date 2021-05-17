valores = 0
for c in range(0, 6):
    x = int(input('Digite um valor inteiro: '))
    if x % 2 == 0:
        valores += x
print(f'A soma dos valores pares é {valores}')
