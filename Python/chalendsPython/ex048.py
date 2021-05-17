soma = 0
cont = 0
for c in range(3, 500, 3):
    if c % 2 == 1:
        cont += 1
        soma += c
print(f'A soma dos {cont} valores é {soma}.')
