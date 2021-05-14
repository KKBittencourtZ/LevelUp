cidade = str(input('Em que cidade você nasceu? ')).upper().strip()
cidadez = cidade.split()
print(cidadez[0] in 'SANTO')

# Alternativa:
# print(cidade[:5] == "SANTO")