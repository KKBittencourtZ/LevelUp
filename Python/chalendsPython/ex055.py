maior = 0
menor = 0
for c in range(1, 6):
    x = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        menor = x
        maior = x
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
print(f'O maior é {maior:.1f}Kg e o menor é {menor:.1f}Kg!')
