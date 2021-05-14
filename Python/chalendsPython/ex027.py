nome = str(input('Digite seu nome completo: ')).strip()
mod = nome.split()
print(
    'Muito prazer em te conhecer!\n'
    f'Seu primeiro nome é {mod[0]}.\n'
    f'Seu último nome é {mod[len(mod) - 1]}.'
)
