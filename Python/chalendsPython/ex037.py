num = int(input('Digite um número inteiro: '))
print(
    'Escolha uma das bases para conversão:\n'
    '[ 1 ] converter para BINÁRIO\n'
    '[ 2 ] converter para OCTAL\n'
    '[ 3 ] converter para HEXADECIMAL'
)
opção = int(input('Sua opção: '))
print(f'{num} convertido para', end=' ')
if opção == 1:
    print(f'BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('NADA é igual a NADA, maus ai ^^')
