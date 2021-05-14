numero = str(input('Informe um número: ')).strip()
calculador = [0, 0, 0, 0]
for c in range(0, len(numero)):
    calculador.append(numero[c])
    calculador.remove(0)
print(f'Analisando o número {numero}')
print(f'Unidade: {calculador[3]}')
print(f'Dezena: {calculador[2]}')
print(f'Centena: {calculador[1]}')
print(f'Milhar: {calculador[0]}')

# Alternaiva matemática seria:
# unidade = numero // 1 % 10
# dezena = numero // 10 % 10
# centena = numero // 100 % 10
# milhar = numero // 1000 % 10
