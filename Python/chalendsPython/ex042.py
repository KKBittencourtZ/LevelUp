seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
tri = [seg1, seg2, seg3]
maior = max(tri)
tri.remove(maior)
if maior > tri[0] + tri[1]:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
    if maior == tri[0] == tri[1]:
        print('EQUILÁTERO!')
    elif maior != tri[0] != tri[1] != maior:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
# ATENÇÃO AO 'elif maior != tri[0] != tri[1] != maior:' o maior no final é o que faz funcionar.
