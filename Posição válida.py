def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    elif orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    return posicoes

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] > 9 or posicao[1] > 9:
            return False
        for navio in frota.values():
            for posicoes_navio in navio:
                if posicao in posicoes_navio:
                    return False
    return True