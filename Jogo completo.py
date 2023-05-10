import random
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

embarcacoes = {1: ['porta-aviões', 4], 2:['navio-tanque', 3], 3:['navio-tanque', 3], 4:['contratorpedeiro', 2], 5:['contratorpedeiro', 2], 6:['contratorpedeiro', 2], 7: ['submarino',1], 8: ['submarino',1], 9: ['submarino',1], 10: ['submarino',1]}
frota = {}
i = 1
while i <= len(embarcacoes):
    nome = embarcacoes[i][0]
    tamanho = embarcacoes[i][1]
    
    print ('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome, tamanho))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if nome != 'submarino':
        orientacao = int(input('Vertical(1) ou Horizontal(2): '))
        
    if orientacao == 1:
        orientacao = 'vertical'
    elif orientacao == 2:
        orientacao = 'horizontal'

    valido = posicao_valida (frota, linha, coluna, orientacao, tamanho)

    if valido == False:
        print('Esta posição não está válida!')
    
    else:
        lista_posicoes = define_posicoes (linha, coluna, orientacao, tamanho)
        frota = preenche_frota (frota, nome, linha, coluna, orientacao, tamanho)
        i += 1

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

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota) 

lista_linha_coluna_ataque_oponente_anterior = []
lista_linha_coluna_ataque_anterior = []
jogando = True
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'
        
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
            
        return texto
    
    print (monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_coluna_invalida = True
    while linha_coluna_invalida:

        linha_invalida = True

        while linha_invalida:
            linha_atacar = int(input('Linha de ataque: '))
            if linha_atacar > 9 or linha_atacar < 0:
                print ('Linha inválida!')
                
            else:
                linha_invalida = False
        
        coluna_invalida = True
    
        while coluna_invalida:
            coluna_atacar = int(input('Coluna de ataque: '))
            if coluna_atacar > 9 or coluna_atacar < 0:
                print ('Coluna inválida!')
                
            else:
                coluna_invalida = False
        
        lista_linha_coluna_ataque = [linha_atacar]
        lista_linha_coluna_ataque. append(coluna_atacar)
        
        if lista_linha_coluna_ataque in lista_linha_coluna_ataque_anterior:
            print ('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atacar, coluna_atacar))
            
        else:
            lista_linha_coluna_ataque_anterior.append(lista_linha_coluna_ataque)
            linha_coluna_invalida = False

    novo_tabuleiro = faz_jogada(tabuleiro_oponente, linha_atacar, coluna_atacar)
    quantos_afundados = afundados(frota_oponente, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

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