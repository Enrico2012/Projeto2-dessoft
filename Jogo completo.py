def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna+i])
    elif orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha+i, coluna])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for x, y in posicao:
                grid[x][y] = 1

    return grid

def afundados(frota, tabuleiro):
    contador = 0
    for tipo, navios in frota.items():
        for navio in navios:
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    break
            else:
                contador += 1
    return contador