cont = soma = maior = menor = 0
while True:
    número = int(input('Digite um número: '))
    cont += 1
    soma += número
    if cont == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        elif número < menor:
            menor = número
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
    else:
        while opção != 'S':
            opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / cont
print(f'Você digitou {cont} números e a média foi {média}')
print(f'O maior valor é {maior} e o menor é {menor}.')
