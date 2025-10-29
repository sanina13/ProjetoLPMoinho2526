from models.Posicao import Posicao as ps
from models.Peca import Peca as pc
from models.Tabuleiro import Tabuleiro as tab


class Movimentos:
    def __init__(self, nivel =None):
        self.nivel = nivel

    
    '''
    Toggle que irá decidir se será manual (jogador) ou automático,
    dependendo do sel.nível
    '''
    def obter_movimento(self, tabuleiro, peca):
        if self.nivel is None:
            return self.obter_movimento_manual(tabuleiro, peca)
        else:
            return self.obter_movimento_auto(tabuleiro, peca, self.nivel)
        
    #
    # Movimento manual(tabuleiro, peca)
    #
    @classmethod
    def obter_movimento_manual(cls, tabuleiro, peca):
        """
        Recebe um tabuleiro e uma peça de um jogador, e devolve um tuplo com
        uma ou duas posições (dependendo da fase).
        Lança ValueError('obter_movimento_manual: escolha invalida') se a jogada for inválida.
        """

        pos_jog = tabuleiro.obter_posicoes_jogador(peca)

        if len(pos_jog) < 3:
            # Fase de colocação
            return cls.fase_colocacao(tabuleiro)
        else:
            # Fase de movimentação
            return cls.fase_movimentacao(tabuleiro, peca, pos_jog)

    # 
    # FASE DE COLOCAÇÃO MANUAL
    # 
    @classmethod
    def fase_colocacao(cls, tabuleiro):
        entrada = input("Turno do jogador. Escolha uma posicao: ").strip().lower()
        
        try:
            if len(entrada) != 2:
                raise ValueError
            pos = ps.cria_posicao(entrada[0], entrada[1])
            if not tabuleiro.eh_posicao_livre(pos):
                raise ValueError
            return (pos,)
        except Exception:
            raise ValueError("obter_movimento_manual: escolha invalida")

    # 
    # FASE DE MOVIMENTAÇÃO MANUAL
    # 
    @classmethod
    def fase_movimentacao(cls, tabuleiro, peca, pos_jog):
        entrada = input("Turno do jogador. Escolha um movimento: ").strip().lower()
        origem, destino = cls.parse_movimento(entrada)

        # Verifica se a origem contém uma peça do jogador
        cls.validar_posicao_jogador(tabuleiro, origem, peca)

        # Se o jogador quiser passar (origem == destino)
        if cls.verificar_passar_turno(tabuleiro, origem, destino, pos_jog):
            return (origem, destino)

        # Verifica se o movimento é válido (livre e adjacente)
        cls.validar_destino(tabuleiro, origem, destino)

        return (origem, destino)
    
    # ==========================
    # AUXILIARES
    # ==========================
    @classmethod
    def peca_do_jogador_na_pos(cls, tabuleiro, pos, peca):
        """Verifica se a posição contém uma peça do jogador."""
        return tabuleiro.posicao_ocupada_por(pos, peca)

    @classmethod
    def existe_movimento_livre(cls, tabuleiro, pos_jog):
        """Verifica se existe alguma peça do jogador que ainda possa mover."""
        for origem in pos_jog:
            for adj in origem.obter_todas_posicoes_perto():
                if tabuleiro.eh_posicao_livre(adj):
                    return True
        return False

    @classmethod
    def parse_movimento(cls, entrada):
        """Lê a string do input e devolve as posições origem e destino."""
        try:
            if len(entrada) != 4:
                raise ValueError
            origem = ps.cria_posicao(entrada[0], entrada[1])
            destino = ps.cria_posicao(entrada[2], entrada[3])
            return origem, destino
        except Exception:
            raise ValueError("obter_movimento_manual: escolha invalida")

    @classmethod
    def validar_posicao_jogador(cls, tabuleiro, origem, peca):
        """Garante que a origem pertence ao jogador."""
        if not cls.peca_do_jogador_na_pos(tabuleiro, origem, peca):
            raise ValueError("obter_movimento_manual: escolha invalida")

    @classmethod
    def verificar_passar_turno(cls, tabuleiro, origem, destino, pos_jog):
        """Valida a regra de passar turno (origem == destino)."""
        if origem.posicoes_iguais(destino):
            if cls.existe_movimento_livre(tabuleiro, pos_jog):
                raise ValueError("obter_movimento_manual: escolha invalida")
            return True
        return False

    @classmethod
    def validar_destino(cls, tabuleiro, origem, destino):
        """Valida se o destino é livre e adjacente."""
        if not tabuleiro.eh_posicao_livre(destino):
            raise ValueError("obter_movimento_manual: escolha invalida")

        if not any(adj.posicoes_iguais(destino) for adj in origem.obter_todas_posicoes_perto()):
            raise ValueError("obter_movimento_manual: escolha invalida")


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
    # obter movimento automático: dispatch para colocação ou movimentação
    @classmethod
    def obter_movimento_auto(cls, tabuleiro, peca, nivel):
        if len(tabuleiro.obter_posicoes_jogador(peca)) < 3:
            return cls.movimento_colocao(tabuleiro, peca)
        else:
            return cls.movimento_movimentacao(tabuleiro, peca, nivel)
        

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
    @classmethod
    def movimento_colocao(cls, tabuleiro, peca):
        posicoes = tabuleiro.obter_posicoes_livres()

        # Vitoria
        condicao = cls.vitoria(tabuleiro, posicoes, peca)
        if condicao:
            return condicao

        # Bloqueio (se 'X', o adversário é 'O', e vice-versa)
        condicao = cls.bloqueio(tabuleiro, posicoes, peca)
        if condicao:
            return condicao

        # Centro
        condicao = cls.centro(tabuleiro)
        if condicao:
            return condicao

        # canto vazio
        condicao = cls.cantos(posicoes)
        if condicao:
            return condicao

        # Laterais Vazias a2, b1, b3, c2
        condicao = cls.laterais(posicoes)
        if condicao:
            return condicao

        # Se nada corresponder
        if posicoes:
            return (posicoes[0],)

    # Funções auxiliares para a fase de colocação

    @classmethod
    def vitoria(cls, tabuleiro, posicoes, peca):
        for pos in posicoes:
            t_sim = tab.cria_copia_tabuleiro(tabuleiro)
            t_sim.coloca_peca(peca, pos)
                    
            if t_sim.obter_ganhador().peca_para_inteiro() == peca.peca_para_inteiro():
                return(pos,) 
    
    @classmethod
    def bloqueio(cls, tabuleiro, posicoes, peca):
        adversario = pc.obter_Peca_adversario(peca)
            
        for pos in posicoes:
            t_sim = tab.cria_copia_tabuleiro(tabuleiro)
            t_sim.coloca_peca(adversario, pos)
                
            if t_sim.obter_ganhador().peca_para_inteiro() == adversario.peca_para_inteiro(): 
                return(pos,)

    @classmethod
    def centro(cls, tabuleiro):
        centro = ps.cria_posicao('b', '2')
        if tabuleiro.eh_posicao_livre(centro):
            return(centro, )

    @classmethod
    def cantos(cls, posicoes):
        cantos = [ps.cria_posicao(l, c) for l in  ['1', '3'] for c in ['a', 'c']]
        for pos in posicoes:
            for canto in cantos:
                if canto.posicoes_iguais(pos):
                    return(pos,) 

    @classmethod
    def laterais(cls, posicoes):
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
    @classmethod
    def movimento_movimentacao(cls, tabuleiro, peca, nivel):
        # testar se existem peças bloqueadas
        posicoes_jogador = tabuleiro.obter_posicoes_jogador(peca)
        
        movimentos_possiveis = cls.movimentosPosiveis(tabuleiro, posicoes_jogador)
        
        #Se não houver movimentos possiveis retorna a primeira posicao do jogador
        if not movimentos_possiveis:
            return (posicoes_jogador[0], posicoes_jogador[0])
        
        # Níveis
        return cls.niveis(tabuleiro, nivel, movimentos_possiveis, peca)

    # Funções auxiliares a movimentação
    @classmethod
    def movimentosPosiveis(cls, tabuleiro, posJogador):
        movimentos_possiveis = []

        for origem in posJogador:
            adjacentes = origem.obter_todas_posicoes_perto()
            for destino in adjacentes:
                if tabuleiro.eh_posicao_livre(destino):
                    movimentos_possiveis.append((origem, destino))
            
        return movimentos_possiveis

    @classmethod
    def niveis(cls, tabuleiro, nivel, movimentosPos, peca):
        if nivel == 'facil':
            return movimentosPos[0]
        
        elif nivel == 'normal':
            resultado, jogadas = cls.minimax(tabuleiro, peca, 1, [])
            if not jogadas:
                return movimentosPos[0]
            melhor_movimento = jogadas[0]
            return melhor_movimento
        
        elif nivel == 'dificil':
            resultado, jogadas = cls.minimax(tabuleiro, peca, 5, [])
            melhor_movimento = jogadas[0]
            return melhor_movimento
    
    #
    # MINIMAX
    #

    '''
        Algoritmo minimax para determinar o melhor movimento possível.
        tabuleiro: estado atual do tabuleiro
        player: jogador atual ('X' ou 'O')
        profundidade: profundidade máxima da busca
        seq_movimentos: sequência de movimentos realizados até o momento
        Testa se o jogo terminou ou se a profundidade máxima foi atingida.
        Se sim, retorna a avaliação do tabuleiro e a sequência de movimentos.
        Caso contrário, explora todos os movimentos possíveis para o jogador atual,
        aplicando recursivamente o minimax para o jogador adversário.
        Retorna o melhor resultado e a sequência de movimentos correspondente.
    '''
    @classmethod
    def minimax(cls, tabuleiro, peca, profundidade, seq_movimentos):  
        if (not tabuleiro.obter_ganhador().pecas_iguais(pc.cria_peca(' '))) or profundidade == 0:
            return tabuleiro.obter_ganhador().peca_para_inteiro(), seq_movimentos
        else:
            melhor_resultado = -2 if peca.peca_para_inteiro() == 1 else 2
            
            melhor_seq_movimentos = seq_movimentos

            for pos in tabuleiro.obter_posicoes_jogador(peca):
                for posAdj in pos.obter_todas_posicoes_perto():
                    if tabuleiro.eh_posicao_livre(posAdj):
                        tab_N = tab.cria_copia_tabuleiro(tabuleiro)
                        tab_N.move_peca(pos, posAdj)

                        peca_adversario = pc.obter_Peca_adversario(peca)

                        novo_resultado, nova_seq_movimentos = cls.minimax(
                            tab_N,
                            peca_adversario,
                            profundidade - 1,
                            seq_movimentos + [(pos, posAdj)]
                        )

                        # Verifica se o resultado é melhor para o jogador atual
                        jogador_eh_x = peca.peca_para_inteiro() == 1
                        if (jogador_eh_x and novo_resultado > melhor_resultado) or (not jogador_eh_x and novo_resultado < melhor_resultado):
                            melhor_resultado, melhor_seq_movimentos = novo_resultado, nova_seq_movimentos
            
            return melhor_resultado, melhor_seq_movimentos
