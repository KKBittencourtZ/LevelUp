def notas(*nota, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return dicionário com várias informações sobre a situação da turma.
    """
    notaz = nota
    maior = max(notaz)
    menor = min(notaz)
    superior = inferior = 0
    for c in range(0, len(notaz)):
        superior += nota[c]
        inferior += 1
    média = superior / inferior
    tudo = {'total': inferior, 'maior': maior, 'menor': menor, 'média':média}
    if sit:
        if média >= 7:
            tudo['situação'] = 'BOA'
        elif média >= 5:
            tudo['situação'] = 'RAZOÁVEL'
        else:
            tudo['situação'] = 'RUIM'
    print('~' * 40)
    return tudo


#Programa principal
resp = notas(5, 6, 7, sit=True)     # É necessário colocar 'sit=True' completo para aparecer na hora de printar!
print(resp)


#Solução do professor
'''
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r
'''