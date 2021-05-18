from time import sleep
x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))
maior = 0
while True:
    sleep(1)
    print('=-=' * 10)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 5:
        print('Finalizando programa...')
        sleep(2)
        break
    elif opção == 1:
        print(f'A soma entre {x} e {y} é {x + y}.')
    elif opção == 2:
        print(f'O resultado de {x} x {y} é {x * y}')
    elif opção == 3:
        if x == y:
            print('Os valores são iguais!')
        else:
            if x > y:
                maior = x
            elif y > x:
                maior = y
            print(f'Entre {x} e {y} o maior valor é {maior}')
    elif opção == 4:
        x = float(input('Primeiro valor: '))
        y = float(input('Segundo valor: '))
    else:
        print('Opção inválida, tente novamente!')
print('Fim do programa! Volte sempre!')
