mais18 = homem = mulher = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        mais18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher += 1
    print('-' * 25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar[0] in 'N':
        print('-' * 25)
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}.')
print(f'Ao todo temos {homem} homem(ns) cadastrados.')
print(f'Temos {mulher} mulher(es) com menos de 20 anos.')
