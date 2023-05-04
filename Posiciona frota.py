def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for x, y in posicao:
                grid[x][y] = 1

    return grid