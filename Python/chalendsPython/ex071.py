print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
nota50 = nota20 = nota10 = nota1 = 0
while valor != 0:
    while valor - 50 >= 0:
        valor -= 50
        nota50 += 1
    while valor - 20 >= 0:
        valor -= 20
        nota20 += 1
    while valor - 10 >= 0:
        valor -= 10
        nota10 += 1
    while valor - 1 >= 0:
        valor -= 1
        nota1 += 1
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota1 != 0:
    print(f'Total de {nota1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
