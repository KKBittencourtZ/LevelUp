frase = str(input('Digite uma frase: ')).upper().strip()
junção = frase.split()
frase_normal = ''
inverso = ''
for c in range(0, len(junção)): # Daria para evitar o uso desse laço com frase_normal = ''.join(junção)
    frase_normal += junção[c]
for c in range(len(frase_normal) - 1, -1, -1):  # Daria para evitar o uso desse laço com inverso = frase_normal[::-1]
    inverso += frase_normal[c]
print(f'O inverso de {frase_normal} é {inverso}')
if frase_normal == inverso:
    print('É um palídromo!')
else:
    print('A frase digitada não é um palíndromo!')
