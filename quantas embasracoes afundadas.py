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