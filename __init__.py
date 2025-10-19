from Posicao import Posicao as ps
from Peca import Peca as pc
from Tabuleiro import Tabuleiro as tab



'''
    Obtém o movimento automático para o jogador indicado, com base no nível de dificuldade.
    Se o jogador tiver menos de 3 peças no tabuleiro, realiza um movimento de colocação
    Se tiver 3 ou mais peças, realiza um movimento de movimentação.
    Tem o nivel de dificuldade que pode ser 'facil', 'normal' ou 'dificil'.
    Em que o nivel facil escolhe o primeiro movimento possivel
    o nivel normal escolhe o melhor movimento com profundidade 1
    o nivel dificil escolhe o melhor movimento com profundidade 5
'''
def obter_movimento_auto(t, peca, nivel):
    if len(t.obter_posicoes_jogador(peca)) < 3:
       return movimento_colocao(t, peca)
    else:
        return movimento_movimentacao(t, peca, nivel)

'''
    Função auxiliar para fase de colocação
    Obtem posições livres e tenta:
    1. Vencer imediatamente
    2. Bloquear vitória do adversário
    3. Colocar no centro se livre
    4. Colocar num canto vazio
    5. Colocar numa lateral vazia
'''
#função auxiliar para fase de movimento colocação
def movimento_colocao(t, peca):
    posicoes = t.obter_posicoes_livres()

    #Vitoria
    for pos in posicoes:
        t_sim = tab.cria_copia_tabuleiro(t)
        t_sim.coloca_peca(peca, pos)
            
        if t_sim.obter_ganhador().peca_para_inteiro() == peca.peca_para_inteiro():
            return(pos,) 
        
    #Bloqueio
    #se 'X', o adversário é 'O', e vice-versa.
    adversario = pc.cria_peca('O' if peca.player == 'X' else 'X')
        
    for pos in posicoes:
        t_sim = tab.cria_copia_tabuleiro(t)
        t_sim.coloca_peca(adversario, pos)
            
        if t_sim.obter_ganhador().peca_para_inteiro() == adversario.peca_para_inteiro(): 
            return(pos,)

    #Centro
    centro = ps.cria_posicao('b', '2')
    if t.eh_posicao_livre(centro):
        return(centro, )
       
    #canto vazio
    """ cantos = [ps.cria_posicao('a', '1').posicao_para_str(), 
                  ps.cria_posicao('a', '3').posicao_para_str(), 
                  ps.cria_posicao('c', '1').posicao_para_str(), 
                  ps.cria_posicao('c', '3').posicao_para_str()] """
    #Versão otimizada com ajuda da ia
    cantos = [ps.cria_posicao(l, c) for l in ['a', 'c'] for c in ['1', '3']]
    for pos in posicoes:
        for canto in cantos:
            if canto.posicoes_iguais(pos):
                return(pos,) 
        
    #Laterais Vazias a2, b1, b3, c2
    """ laterais = [ps.cria_posicao('a', '2').posicao_para_str(), 
                  ps.cria_posicao('b', '1').posicao_para_str(), 
                  ps.cria_posicao('b', '3').posicao_para_str(), 
                  ps.cria_posicao('c', '2').posicao_para_str()]  """
    laterais = [ps.cria_posicao(l,c) for l, c in [('a', '2'), ('b', '1'), ('b', '3'), ('c', '2')]]
    for pos in posicoes:
        for lateral in laterais:
            if lateral.posicoes_iguais(pos):
                return(pos,)
            
'''
    Função auxiliar para fase de movimentação
    Obtem todas as peças do jogador e verifica as posições adjacentes livres
    e cria uma lista de movimentos possíveis (origem, destino).
    Se não houver movimentos possíveis (peças bloqueadas), retorna a primeira posição do jogador.
    Dependendo do nível de dificuldade, escolhe o movimento:
    - 'facil': o primeiro movimento possível.
    - 'normal': o melhor movimento usando minimax com profundidade 1.
    - 'dificil': o melhor movimento usando minimax com profundidade 5.
'''
def movimento_movimentacao(t, peca, nivel):
    # testar se existem peças bloqueadas
    posicoes_jogador = t.obter_posicoes_jogador(peca)
    
    movimentos_possiveis = []

    for origem in posicoes_jogador:
        adjacentes = origem.obter_posicoes_adjacentes()
        for destino in adjacentes:
            if t.eh_posicao_livre(destino):
                movimentos_possiveis.append((origem, destino))

    #Se não houver movimentos possiveis retorna a primeira posicao do jogador
    if not movimentos_possiveis:
        primeira = posicoes_jogador[0]
        return (primeira, primeira)
    
    # Níveis

    '''facil a peça a movimentar é sempre a que ocupa a primeira posição em
    ordem de leitura do tabuleiro que tenha alguma posição adjacente livre. A posição de
    destino é a primeira posição adjacente livre.'''

    if nivel == 'facil':
        return movimentos_possiveis[0]

    #normal a incluir o algoritmo minimax

    elif nivel == 'normal':
      resultado, jogadas = minimax(t, peca.player, 1, [])
      if not jogadas:
          return movimentos_possiveis[0]
      melhor_movimento = jogadas[0]
      return melhor_movimento
    
    elif nivel == 'dificil':
        resultado, jogadas = minimax(t, peca.player, 5, [])
        melhor_movimento = jogadas[0]
        return melhor_movimento




'''
    Algoritmo minimax para determinar o melhor movimento possível.
    t: estado atual do tabuleiro
    player: jogador atual ('X' ou 'O')
    profundidade: profundidade máxima da busca
    seq_movimentos: sequência de movimentos realizados até o momento
    Testa se o jogo terminou ou se a profundidade máxima foi atingida.
    Se sim, retorna a avaliação do tabuleiro e a sequência de movimentos.
    Caso contrário, explora todos os movimentos possíveis para o jogador atual,
    aplicando recursivamente o minimax para o jogador adversário.
    Retorna o melhor resultado e a sequência de movimentos correspondente.
'''
def minimax(t, player, profundidade, seq_movimentos):  
    if (not t.obter_ganhador().pecas_iguais(pc.cria_peca(' '))) or profundidade == 0:
        return t.obter_ganhador().peca_para_inteiro(), seq_movimentos
    else:

        melhor_resultado = -2 if player == 'X' else 2
        
        melhor_seq_movimentos = seq_movimentos

        #Jogador peca para iterar no loop ...
        player_peca = pc.cria_peca(player)

        for pos in t.obter_posicoes_jogador(player_peca):
            for posAdj in pos.obter_posicoes_adjacentes():
                if t.eh_posicao_livre(posAdj):
                    tab_N = tab.cria_copia_tabuleiro(t)
                    tab_N.move_peca(pos, posAdj)

                    outro_player = 'X' if player == 'O' else 'O'

                    novo_resultado, nova_seq_movimentos = minimax(
                        tab_N,
                        outro_player,
                        profundidade - 1,
                        seq_movimentos + [(pos, posAdj)]
                    )

                    # da para remover esse not in locals mas o professor colocou no pseudo-codigo
                    if 'melhor_seq_movimentos' not in locals() or (player == 'X' and novo_resultado > melhor_resultado) or (player == 'O' and novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = novo_resultado, nova_seq_movimentos        
        
        return melhor_resultado, melhor_seq_movimentos

t = tab.cria_tabuleiro() 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'facil') 
print(ps.posicao_para_str(m[0]))

t = tab.tuplo_para_tabuleiro(((1,0,-1),(0,1,-1),(1,-1,0))) 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'facil') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

m = obter_movimento_auto(t, pc.cria_peca('X'), 'normal') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

t = tab.tuplo_para_tabuleiro(((1,-1,-1),(-1,1,0),(0,0,1))) 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'normal') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

m = obter_movimento_auto(t, pc.cria_peca('X'), 'dificil') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))


#testes anteriores


""" p1 = pos.cria_posicao('a', '2')
p2 = pos.cria_posicao('a', '3')

print(p1.posicoes_iguais(p2))

print(pos.posicao_para_str(p1)) # verificar pelicas se tem que printar com elas
print(isinstance(pos.posicao_para_str(p1), str)) # indicar ser String

print(tuple(pos.posicao_para_str(p) for p in pos.obter_posicoes_adjacentes(p2)))

j1 = pc.cria_peca('X')
j2 = pc.cria_peca('X')

print(j1.pecas_iguais(j2))
print(pc.peca_para_str(j1))
print(pc.peca_para_inteiro(pc.cria_peca(' ')))

tabuleiro = tab.cria_tabuleiro()

for linha in tabuleiro.tabuleiro_lista:
    for peca in linha:
        print("["+ pc.peca_para_str(peca) +"]", end='')
    print() 

tabuleiro.coloca_peca(j1, p1)
vet = tabuleiro.obter_vetor('2')
print([pc.peca_para_str(p) for p in vet]) """




        