#http://pt.stackoverflow.com/questions/183618/exerc%C3%ADcio-em-python-similaridade-entre-textos

import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = (sum(abs(a - b) for a, b in zip(as_a, as_b)))
    sab = soma / 6
    return sab
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto. '''
    listasentencas = separa_sentencas(texto)
    tamanho = 0
    lista_n_palavras = []
    for sentenca in listasentencas:
        listafrases = separa_frases(sentenca)
        for frase in listafrases:
            lista_palavras = separa_palavras(frase)
            for palavra in lista_palavras:
                lista_n_palavras.append(palavra)
                tamanho = len(palavra) + tamanho
            tamanho_medio_palavra = tamanho/len(lista_n_palavras)
            relacao_type_token = n_palavras_diferentes(lista_palavras)/len(lista_n_palavras)
            razao_hapax_legomana = n_palavras_unicas(lista_palavras)/len(lista_n_palavras)
            tamanho_medio_sentenca = len(listasentencas)+len(listasentencas)/len(listasentencas)
            complex_sentenca = len(listafrases)/len(listasentencas)
            tamanho_medio_frase = len(listafrases)/len(frase)

    return [tamanho_medio_palavra, relacao_type_token, razao_hapax_legomana, tamanho_medio_sentenca, tamanho_medio_frase] 
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass
