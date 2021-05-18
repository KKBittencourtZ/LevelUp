soma = cont = 0
while True:
    x = int(input('Digite um número  [999 para parar]: '))
    if x == 999:
        break
    else:
        cont += 1
        soma += x
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
