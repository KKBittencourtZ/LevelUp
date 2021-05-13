from random import randint
aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))
integrantes = (aluno_1, aluno_2, aluno_3, aluno_4)
roleta = randint(0, 5)
print(roleta)
print(f'O aluno escolhido foi {integrantes[roleta]}')

# Outro método é usando random.choice mas usando lista no lugar da tupla que estão os integrantes.