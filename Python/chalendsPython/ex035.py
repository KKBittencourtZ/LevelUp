print('Diga o comprimento de três retas para ver se podem formar um triângulo')
reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))
retas = [reta1, reta2, reta3]
hip = max(retas)
retas.pop(retas.index(max(retas)))
if hip < retas[0] + retas[1]:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
