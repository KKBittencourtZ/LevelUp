números = [[], []]
for c in range(1, 8):
    x = int(input(f'Digite o {c}º valor: '))
    if x % 2 == 0:
        números[0].append(x)
    else:
        números[1].append(x)
print('-=' * 20)
números[0].sort()
números[1].sort()
print(f'Os valores pares digitados foram: {números[0]}')
print(f'Os valores ímpares digitados foram: {números[1]}')
