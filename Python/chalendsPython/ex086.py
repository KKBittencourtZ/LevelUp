coluna = fileira = 0
matriz = []
for c in range(0, 9):
    matriz.append(int(input(f'Digite um valor para [{coluna}, {fileira}]: ')))
    fileira += 1
    if fileira == 3:
        coluna += 1
        fileira = 0
print('-=' * 20)
for n, v in enumerate(matriz):
    print(f'[{v:^5}]', end=' ')
    if n == 2 or n == 5:
        print()
print()
# Resolução do professor
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''