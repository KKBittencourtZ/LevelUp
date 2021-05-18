print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
for c in range(0, 19):
    if c % 2 == 0:
        p = c
    else:
        i = c
        print(f'{listagem[p]:.<28}R$ {listagem[i]:>8.2f}')
print('-' * 40)
