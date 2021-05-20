cadastro_de_notas = [[], [], [], []]
localizador = 0
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    cadastro_de_notas[0].append(nome)
    cadastro_de_notas[1].append(nota1)
    cadastro_de_notas[2].append(nota2)
    cadastro_de_notas[3].append(média)
    novo_cadastro = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while novo_cadastro not in 'SN':
        novo_cadastro = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if novo_cadastro == 'N':
        break
print('-=' * 20)
print('N  NOME                 MÉDIA')
print('------------------------------')
for n, m in enumerate(cadastro_de_notas[0]):
    print(f'{n}  {m:<20}  {cadastro_de_notas[3][n]:.1f}')
print('------------------------------')
print('    PARA PARAR DIGITE [999]')
print('------------------------------')
while localizador != 999:
    seletor = int(input('Qual aluno gostaria de ver a nota? '))
    localizador = seletor
    if seletor > len(cadastro_de_notas[0]) - 1 and seletor != 999:
        print('Aluno não cadastrado')
    elif seletor <= len(cadastro_de_notas[0]) - 1:
        print(f'Notas de {cadastro_de_notas[0][seletor]} são {cadastro_de_notas[1][seletor]} e {cadastro_de_notas[2][seletor]}')
print('------------------------------')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
