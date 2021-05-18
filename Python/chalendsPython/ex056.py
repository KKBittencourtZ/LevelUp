soma = 0
idade_velho = 0
nome_velho = ''
contm = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        contm += 1
média = soma / 4
print(f'A média de idade do grupo é de {média:.1f} anos.')
if idade_velho != 0:
    print(f'O homem mais velho tem {idade_velho} anos e se chama {nome_velho}.')
else:
    print('Não tem homem entre as pessoas indicadas.')
print(f'Ao todo são {contm} mulheres com menos de 20 anos.')
