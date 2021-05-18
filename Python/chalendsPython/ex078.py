x = []
for c in range(0, 5):
    x. append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'Você digitou os valores {x}')
print(f'O maior valor digitado foi {max(x)} nas posições', end=' ')
for v in range(0, 5):
    if x[v] == max(x):
        print(v, end=' ')
print(f'\nO menor valor digitado foi {min(x)} nas posições', end=' ')
for v in range(0, 5):
    if x[v] == min(x):
        print(v, end=' ')
print()
