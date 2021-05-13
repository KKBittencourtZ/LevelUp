largura_parede = float(input('Largura da parede: '))
altura_parede = float(input('Altura da parede: '))
area = largura_parede * altura_parede
print(f'Sua parede tem a dimensão de {largura_parede}x{altura_parede} e sua área é de {area:.2f}m².')
print(f'Para pintar essa parede, você precisará de {area/2:.2f}l de tinta')