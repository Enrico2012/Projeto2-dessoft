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
