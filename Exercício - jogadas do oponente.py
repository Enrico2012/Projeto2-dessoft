import random

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


frota = {}

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

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota) 

lista_linha_coluna_ataque_oponente_anterior = []
lista_linha_coluna_ataque_anterior = []

linha_coluna_oponente_invalida = True
while linha_coluna_oponente_invalida:
    linha_ataque_oponente = random.randint(0,9)
    coluna_ataque_oponente = random.randint(0,9)
        
    lista_linha_coluna_ataque_oponente = [linha_ataque_oponente, coluna_ataque_oponente]
        
    if lista_linha_coluna_ataque_oponente not in lista_linha_coluna_ataque_oponente_anterior:
        lista_linha_coluna_ataque_oponente_anterior.append(lista_linha_coluna_ataque_oponente)
        linha_coluna_oponente_invalida = False
        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente, coluna_ataque_oponente))
        novo_tabuleiro = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
        quantos_afundados = afundados (frota, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False