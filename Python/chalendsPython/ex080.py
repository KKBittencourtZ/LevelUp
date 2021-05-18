valores = []
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0 or x > valores[-1]:
        valores.append(x)
    else:
        pos = 0
        while pos < len(valores):
            if x <= valores[pos]:
                valores.insert(pos, x)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
