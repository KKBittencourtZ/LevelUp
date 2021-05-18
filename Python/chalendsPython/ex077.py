x = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for v in range(0, len(x)):
    print(f'Na palavra {x[v]} temos ', end='')
    for c in range(0, len(x[v])):
        if x[v][c] in 'AEIOUY':
            print(x[v][c].lower(), end=' ')
    print()
