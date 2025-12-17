from models.Tabuleiro import *


#   MOVIMENTO MANUAL OU AUTOMATICO


def obter_movimento(tabuleiro, peca, nivel=None):
    """
    Decide se sera manual (jogador) ou automatico,
    dependendo se o nivel foi passado como argumento.
    """
    if nivel is None:
        return obter_movimento_manual(tabuleiro, peca)
    else:
        return obter_movimento_auto(tabuleiro, peca, nivel)



#   MOVIMENTO MANUAL


def obter_movimento_manual(tabuleiro, peca):
    """
    Recebe um tabuleiro e uma peca de um jogador, e devolve um tuplo com
    uma ou duas posicoes (dependendo da fase).
    Lanca ValueError('obter_movimento_manual: escolha invalida') se a jogada for invalida.
    """
    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca)

    if len(posicoes_jogador) < 3:
        return fase_colocacao(tabuleiro)
    else:
        return fase_movimentacao(tabuleiro, peca, posicoes_jogador)


def fase_colocacao(tabuleiro):
    jogada_validada = False
    while not jogada_validada:
        entrada_jogador = input("Turno do jogador. Escolha uma posicao (ex: a1, coluna a-c, linha 1-3): ").strip().lower()

        try:
            if len(entrada_jogador) != 2:
                raise ValueError
            posicao = cria_posicao(entrada_jogador[0], entrada_jogador[1])
            if not eh_posicao_livre(tabuleiro, posicao):
                raise ValueError
            jogada_validada = True
            return (posicao,)
        except Exception:
            print("Escolha invalida. Formato esperado: 'a1' (coluna a-c, linha 1-3). Tente novamente.")
        


def fase_movimentacao(tabuleiro, peca, posicoes_jogador):
    jogada_validada = False
    while not jogada_validada:
        try:
            entrada_jogador = input("Turno do jogador. Escolha um movimento (ex: a1b2, origem+destino): ").strip().lower()
        except EOFError:
            # Em ambiente de testes (stdin esgotado), propagamos como ValueError para manter compatibilidade
            raise ValueError("obter_movimento_manual: escolha invalida")

        # Primeiro tente interpretar o formato (origem+destino)
        try:
            posicao_origem, posicao_destino = parse_movimento(entrada_jogador)
        except ValueError:
            print("Formato invalido. Formato esperado: 'a1b2' (origem+destino). Tente novamente.")
            continue

        # Agora valide semanticamente a jogada (pertence ao jogador, destino livre/adjacente)
        try:
            validar_posicao_jogador(tabuleiro, posicao_origem, peca)

            if verificar_passar_turno(tabuleiro, posicao_origem, posicao_destino, posicoes_jogador):
                jogada_validada = True
                return (posicao_origem, posicao_destino)

            validar_destino(tabuleiro, posicao_origem, posicao_destino)
            jogada_validada = True
            return (posicao_origem, posicao_destino)
        except ValueError:
            print("Movimento invalido: origem nao e sua peca, destino ocupado ou nao adjacente. Tente novamente.")
            continue



# AUXILIARES (MANUAL)


def peca_do_jogador_na_pos(tabuleiro, posicao, peca):
    """Verifica se a posicao contem uma peca do jogador."""
    return pecas_iguais(obter_peca(tabuleiro, posicao), peca)


def existe_movimento_livre(tabuleiro, posicoes_jogador):
    """Verifica se existe alguma peca do jogador que ainda possa mover."""
    for posicao_origem in posicoes_jogador:
        for posicao_adj in obter_posicoes_adjacentes(posicao_origem):
            if eh_posicao_livre(tabuleiro, posicao_adj):
                return True
    return False


def parse_movimento(entrada_movimento):
    """Le a string do input e devolve as posicoes origem e destino."""
    try:
        if len(entrada_movimento) != 4:
            raise ValueError
        posicao_origem = cria_posicao(entrada_movimento[0], entrada_movimento[1])
        posicao_destino = cria_posicao(entrada_movimento[2], entrada_movimento[3])
        return posicao_origem, posicao_destino
    except Exception:
        raise ValueError("obter_movimento_manual: escolha invalida")


def validar_posicao_jogador(tabuleiro, posicao_origem, peca):
    """Garante que a origem pertence ao jogador."""
    if not peca_do_jogador_na_pos(tabuleiro, posicao_origem, peca):
        raise ValueError("obter_movimento_manual: escolha invalida")


def verificar_passar_turno(tabuleiro, posicao_origem, posicao_destino, posicoes_jogador):
    """Valida a regra de passar turno (origem == destino)."""
    if posicoes_iguais(posicao_origem, posicao_destino):
        if existe_movimento_livre(tabuleiro, posicoes_jogador):
            raise ValueError("obter_movimento_manual: escolha invalida")
        return True
    return False


def validar_destino(tabuleiro, posicao_origem, posicao_destino):
    """Valida se o destino e livre e adjacente."""
    if not eh_posicao_livre(tabuleiro, posicao_destino):
        raise ValueError("obter_movimento_manual: escolha invalida")

    if posicao_destino not in obter_posicoes_adjacentes(posicao_origem):
        raise ValueError("obter_movimento_manual: escolha invalida")


#   MOVIMENTO AUTOMATICO

def obter_movimento_auto(tabuleiro, peca, nivel):
    """
    Obtem o movimento automatico para o jogador indicado com base no nivel de dificuldade.
    """
    if len(obter_posicoes_jogador(tabuleiro, peca)) < 3:
        return movimento_colocacao(tabuleiro, peca)
    else:
        return movimento_movimentacao(tabuleiro, peca, nivel)


#   FASE DE COLOCACAO AUTOMATICA

def movimento_colocacao(tabuleiro, peca):
    posicoes_livres = obter_posicoes_livres(tabuleiro)

    resultado = vitoria(tabuleiro, posicoes_livres, peca)
    if resultado:
        return resultado

    resultado = bloqueio(tabuleiro, posicoes_livres, peca)
    if resultado:
        return resultado

    resultado = centro(tabuleiro)
    if resultado:
        return resultado

    resultado = cantos(posicoes_livres)
    if resultado:
        return resultado

    resultado = laterais(posicoes_livres)
    if resultado:
        return resultado

    if posicoes_livres:
        return (posicoes_livres[0],)


def vitoria(tabuleiro, posicoes_livres, peca):
    for posicao_livre in posicoes_livres:
        tabuleiro_simulado = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(tabuleiro_simulado, peca, posicao_livre)
        if pecas_iguais(obter_ganhador(tabuleiro_simulado), peca):
            return (posicao_livre,)


def bloqueio(tabuleiro, posicoes_livres, peca):
    adversario = obter_peca_adversario(peca)
    for posicao_livre in posicoes_livres:
        tabuleiro_simulado = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(tabuleiro_simulado, adversario, posicao_livre)
        if pecas_iguais(obter_ganhador(tabuleiro_simulado), adversario):
            return (posicao_livre,)


def centro(tabuleiro):
    posicao_centro = cria_posicao('b', '2')
    if eh_posicao_livre(tabuleiro, posicao_centro):
        return (posicao_centro,)


def cantos(posicoes_livres):
    lista_cantos = [cria_posicao(c, l) for c, l in [('a', '1'), ('a', '3'), ('c', '1'), ('c', '3')]]
    for posicao_livre in posicoes_livres:
        if posicao_livre in lista_cantos:
            return (posicao_livre,)


def laterais(posicoes_livres):
    lista_laterais = [cria_posicao(c, l) for c, l in [('a', '2'), ('b', '1'), ('b', '3'), ('c', '2')]]
    for posicao_livre in posicoes_livres:
        if posicao_livre in lista_laterais:
            return (posicao_livre,)


#   FASE DE MOVIMENTACAO AUTOMATICA

def movimento_movimentacao(tabuleiro, peca, nivel):
    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca)
    movimentos_disponiveis = movimentos_possiveis(tabuleiro, posicoes_jogador)

    if not movimentos_disponiveis:
        return (posicoes_jogador[0], posicoes_jogador[0])

    if nivel == 'facil':
        return movimentos_disponiveis[0]
    elif nivel == 'normal':
        resultado_minimax, lista_jogadas = minimax(tabuleiro, peca, 1, [])
        return lista_jogadas[0] if lista_jogadas else movimentos_disponiveis[0]
    elif nivel == 'dificil':
        resultado_minimax, lista_jogadas = minimax(tabuleiro, peca, 5, [])
        return lista_jogadas[0]


def movimentos_possiveis(tabuleiro, posicoes_jogador):
    movimentos = []
    for posicao_origem in posicoes_jogador:
        for posicao_destino in obter_posicoes_adjacentes(posicao_origem):
            if eh_posicao_livre(tabuleiro, posicao_destino):
                movimentos.append((posicao_origem, posicao_destino))
    return movimentos


#   MINIMAX

def minimax(tabuleiro, peca, profundidade, sequencia_movimentos):
    if not pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')) or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(tabuleiro)), sequencia_movimentos

    melhor_resultado = -2 if peca_para_inteiro(peca) == 1 else 2
    melhor_sequencia = sequencia_movimentos

    for posicao_origem in obter_posicoes_jogador(tabuleiro, peca):
        for posicao_destino in obter_posicoes_adjacentes(posicao_origem):
            if eh_posicao_livre(tabuleiro, posicao_destino):
                tabuleiro_simulado = cria_copia_tabuleiro(tabuleiro)
                move_peca(tabuleiro_simulado, posicao_origem, posicao_destino)
                peca_adversario = obter_peca_adversario(peca)

                novo_resultado, nova_sequencia = minimax(
                    tabuleiro_simulado,
                    peca_adversario,
                    profundidade - 1,
                    sequencia_movimentos + [(posicao_origem, posicao_destino)]
                )

                jogador_x = peca_para_inteiro(peca) == 1
                if (jogador_x and novo_resultado > melhor_resultado) or \
                   (not jogador_x and novo_resultado < melhor_resultado):
                    melhor_resultado, melhor_sequencia = novo_resultado, nova_sequencia

    return melhor_resultado, melhor_sequencia
