from models.Posicao import Posicao as ps
from models.Peca import Peca as pc
from models.Tabuleiro import Tabuleiro as tab


class Movimentos:
    def __init__(self):
        pass

    
    '''
    Toggle que irá decidir se será manual (jogador) ou automático,
    dependendo do sel.nível
    '''
    def obter_movimento(self, t, peca):
        if self.nivel is None:
            return self.obter_movimento_manual(t, peca)
        else:
            return self.obter_movimento_auto(t, peca, self.nivel)
    #
    # Espaço para o movimento manual(t, peca)
    #
    def obter_movimento_manual(self, t, peca):
        print('teste')


    #
    # MOVIMENTO AUTO
    #
    
    '''
    Obtém o movimento automático para o jogador indicado, com base no nível de dificuldade.
    Se o jogador tiver menos de 3 peças no tabuleiro, realiza um movimento de colocação
    Se tiver 3 ou mais peças, realiza um movimento de movimentação.
    Tem o nivel de dificuldade que pode ser 'facil', 'normal' ou 'dificil'.
    Em que o nivel facil escolhe o primeiro movimento possivel
    o nivel normal escolhe o melhor movimento com profundidade 1
    o nivel dificil escolhe o melhor movimento com profundidade 5
    '''
    # !!! Verificar se usar static aqui é melhor forma
    @staticmethod
    def obter_movimento_auto(t, peca, nivel):
        if len(t.obter_posicoes_jogador(peca)) < 3:
            return Movimentos.movimento_colocao(t, peca)
        else:
            return Movimentos.movimento_movimentacao(t, peca, nivel)
        

    #
    # FASE DE COLOCAÇÃO
    #

    '''
    Função auxiliar para fase de colocação
    Obtem posições livres e tenta:
    1. Vencer imediatamente
    2. Bloquear vitória do adversário
    3. Colocar no centro se livre
    4. Colocar num canto vazio
    5. Colocar numa lateral vazia
    '''
    @staticmethod
    def movimento_colocao(t, peca):
        posicoes = t.obter_posicoes_livres()

        #Vitoria
        condicao = Movimentos.vitoria(t, posicoes, peca)
        if condicao: return condicao
                
        #Bloqueio
        #se 'X', o adversário é 'O', e vice-versa.
        condicao = Movimentos.bloqueio(t, posicoes, peca)
        if condicao: return condicao

        #Centro
        condicao = Movimentos.centro(t)
        if condicao: return condicao
            
        #canto vazio
        condicao = Movimentos.cantos(posicoes)
        if condicao: return condicao
                
        #Laterais Vazias a2, b1, b3, c2
        condicao = Movimentos.laterais(posicoes)
        if condicao: return condicao

        # Se nada corresponder 
        if posicoes:                     
            return (posicoes[0],)

    # Funções auxiliares para a fase de colocação

    @staticmethod
    def vitoria(t, posicoes, peca):
        for pos in posicoes:
            t_sim = tab.cria_copia_tabuleiro(t)
            t_sim.coloca_peca(peca, pos)
                    
            if t_sim.obter_ganhador().peca_para_inteiro() == peca.peca_para_inteiro():
                return(pos,) 
    
    @staticmethod
    def bloqueio(t, posicoes, peca):
        adversario = pc.cria_peca('O' if peca.player == 'X' else 'X')
            
        for pos in posicoes:
            t_sim = tab.cria_copia_tabuleiro(t)
            t_sim.coloca_peca(adversario, pos)
                
            if t_sim.obter_ganhador().peca_para_inteiro() == adversario.peca_para_inteiro(): 
                return(pos,)

    @staticmethod
    def centro(t):
        centro = ps.cria_posicao('b', '2')
        if t.eh_posicao_livre(centro):
            return(centro, )

    @staticmethod
    def cantos(posicoes):
        cantos = [ps.cria_posicao(l, c) for l in ['a', 'c'] for c in ['1', '3']]
        for pos in posicoes:
            for canto in cantos:
                if canto.posicoes_iguais(pos):
                    return(pos,) 

    @staticmethod
    def laterais(posicoes):
        laterais = [ps.cria_posicao(l,c) for l, c in [('a', '2'), ('b', '1'), ('b', '3'), ('c', '2')]]
        for pos in posicoes:
            for lateral in laterais:
                if lateral.posicoes_iguais(pos):
                    return(pos,)

    #
    # FASE DE MOVIMENTAÇÃO
    #

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
    @staticmethod
    def movimento_movimentacao(t, peca, nivel):
        # testar se existem peças bloqueadas
        posicoes_jogador = t.obter_posicoes_jogador(peca)
        
        movimentos_possiveis = Movimentos.movimentosPosiveis(t, posicoes_jogador)
        
        #Se não houver movimentos possiveis retorna a primeira posicao do jogador
        if not movimentos_possiveis:
            primeira = posicoes_jogador[0]
            return (primeira, primeira)
        
        # Níveis
        return Movimentos.niveis(t, nivel, movimentos_possiveis, peca)

    # Funções auxiliares a movimentação
    @staticmethod
    def movimentosPosiveis(t, posJogador):
        movimentos_possiveis = []

        for origem in posJogador:
            adjacentes = origem.obter_todas_posicoes_perto()
            for destino in adjacentes:
                if t.eh_posicao_livre(destino):
                    movimentos_possiveis.append((origem, destino))
            
        return movimentos_possiveis

    @staticmethod
    def niveis(t, nivel, movimentosPos, peca):
        if nivel == 'facil':
            return movimentosPos[0]
        
        elif nivel == 'normal':
            resultado, jogadas = Movimentos.minimax(t, peca.player, 1, [])
            if not jogadas:
                return movimentosPos[0]
            melhor_movimento = jogadas[0]
            return melhor_movimento
        
        elif nivel == 'dificil':
            resultado, jogadas = Movimentos.minimax(t, peca.player, 5, [])
            melhor_movimento = jogadas[0]
            return melhor_movimento
    
    #
    # MINIMAX
    #

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
    @staticmethod
    def minimax(t, player, profundidade, seq_movimentos):  
        if (not t.obter_ganhador().pecas_iguais(pc.cria_peca(' '))) or profundidade == 0:
            return t.obter_ganhador().peca_para_inteiro(), seq_movimentos
        else:

            melhor_resultado = -2 if player == 'X' else 2
            
            melhor_seq_movimentos = seq_movimentos

            #Jogador peca para iterar no loop ...
            player_peca = pc.cria_peca(player)

            for pos in t.obter_posicoes_jogador(player_peca):
                for posAdj in pos.obter_todas_posicoes_perto():
                    if t.eh_posicao_livre(posAdj):
                        tab_N = tab.cria_copia_tabuleiro(t)
                        tab_N.move_peca(pos, posAdj)

                        outro_player = 'X' if player == 'O' else 'O'

                        novo_resultado, nova_seq_movimentos = Movimentos.minimax(
                            tab_N,
                            outro_player,
                            profundidade - 1,
                            seq_movimentos + [(pos, posAdj)]
                        )

                        # da para remover esse not in locals mas o professor colocou no pseudo-codigo
                        if 'melhor_seq_movimentos' not in locals() or (player == 'X' and novo_resultado > melhor_resultado) or (player == 'O' and novo_resultado < melhor_resultado):
                            melhor_resultado, melhor_seq_movimentos = novo_resultado, nova_seq_movimentos        
            
            return melhor_resultado, melhor_seq_movimentos