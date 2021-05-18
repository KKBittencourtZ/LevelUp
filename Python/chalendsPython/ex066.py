cont = soma = 0
while True:
    x = int(input('Digite um valor  (999 para parar): '))
    if x == 999:
        break
    cont += 1
    soma += x
print(f'A soma dos {cont} valores foi {soma}!')
