from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
ang_rad = radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {sin(ang_rad):.2f}.')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(ang_rad):.2f}.')
print(f'O ângulo de {angulo} tem a TANGENTE de {tan(ang_rad):.2f}')
