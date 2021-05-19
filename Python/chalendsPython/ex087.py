números = []
coluna = linha = pares = coluna3 = 0
for c in range(1, 10):
    números.append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))
    coluna += 1
    if coluna == 3:
        linha += 1
        coluna = 0
print('-=' * 20)
for c, l in enumerate(números):
    print(f'[{l:^5}]', end=' ')
    if c == 2 or c == 5 or c == 8:
        coluna3 += l
        print()
    if l % 2 == 0:
        pares += l
print('-=' * 20)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {max(números[3:6])}.')
