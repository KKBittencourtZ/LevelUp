cadastros = []
temp = {}
soma = 0
while True:
    temp['Nome'] = str(input('Nome: ')).strip().capitalize()
    temp['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    while temp['Sexo'] not in 'FM':
        print('ERRO! Apenas F ou M.')
        temp['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
    temp['Idade'] = int(input('Idade: '))
    cadastros.append(temp.copy())
    soma += temp['Idade']
    pergunta = str(input('Quer continuar? ')).strip().upper()[0]
    while pergunta not in 'SN':
        print('ERRO! Apenas S ou N.')
        pergunta = str(input('Quer continuar? ')).strip().upper()[0]
    if pergunta == 'N':
        break
média = soma / len(cadastros)
print('~ ' * 25)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastras.')
print(f'B) A média de idade é de {média:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for i, n in enumerate(cadastros):
    if n['Sexo'] == 'F':
        print(f'{n["Nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for i, k in enumerate(cadastros):
    if cadastros[i]['Idade'] > média:
        print(f'nome = {k["Nome"]}; sexo = {k["Sexo"]}; idade = {k["Idade"]}')
