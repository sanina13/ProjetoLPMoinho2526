from models.tabuleiro import *

# ==========================================================
#   MOVIMENTO MANUAL OU AUTOMÁTICO
# ==========================================================

def obter_movimento(tabuleiro, peca, nivel=None):
    """
    Decide se será manual (jogador) ou automático,
    dependendo se o nível foi passado como argumento.
    """
    if nivel is None:
        return obter_movimento_manual(tabuleiro, peca)
    else:
        return obter_movimento_auto(tabuleiro, peca, nivel)


# ==========================================================
#   MOVIMENTO MANUAL
# ==========================================================

def obter_movimento_manual(tabuleiro, peca):
    """
    Recebe um tabuleiro e uma peça de um jogador, e devolve um tuplo com
    uma ou duas posições (dependendo da fase).
    Lança ValueError('obter_movimento_manual: escolha invalida') se a jogada for inválida.
    """
    pos_jog = obter_posicoes_jogador(tabuleiro, peca)

    if len(pos_jog) < 3:
        return fase_colocacao(tabuleiro)
    else:
        return fase_movimentacao(tabuleiro, peca, pos_jog)


def fase_colocacao(tabuleiro):
    entrada = input("Turno do jogador. Escolha uma posicao: ").strip().lower()

    try:
        if len(entrada) != 2:
            raise ValueError
        pos = cria_posicao(entrada[0], entrada[1])
        if not eh_posicao_livre(tabuleiro, pos):
            raise ValueError
        return (pos,)
    except Exception:
        raise ValueError("obter_movimento_manual: escolha invalida")


def fase_movimentacao(tabuleiro, peca, pos_jog):
    entrada = input("Turno do jogador. Escolha um movimento: ").strip().lower()
    origem, destino = parse_movimento(entrada)

    validar_posicao_jogador(tabuleiro, origem, peca)

    if verificar_passar_turno(tabuleiro, origem, destino, pos_jog):
        return (origem, destino)

    validar_destino(tabuleiro, origem, destino)
    return (origem, destino)


# ==========================
# AUXILIARES (MANUAL)
# ==========================

def peca_do_jogador_na_pos(tabuleiro, pos, peca):
    """Verifica se a posição contém uma peça do jogador."""
    return pecas_iguais(obter_peca(tabuleiro, pos), peca)


def existe_movimento_livre(tabuleiro, pos_jog):
    """Verifica se existe alguma peça do jogador que ainda possa mover."""
    for origem in pos_jog:
        for adj in obter_posicoes_adjacentes(origem):
            if eh_posicao_livre(tabuleiro, adj):
                return True
    return False


def parse_movimento(entrada):
    """Lê a string do input e devolve as posições origem e destino."""
    try:
        if len(entrada) != 4:
            raise ValueError
        origem = cria_posicao(entrada[0], entrada[1])
        destino = cria_posicao(entrada[2], entrada[3])
        return origem, destino
    except Exception:
        raise ValueError("obter_movimento_manual: escolha invalida")


def validar_posicao_jogador(tabuleiro, origem, peca):
    """Garante que a origem pertence ao jogador."""
    if not peca_do_jogador_na_pos(tabuleiro, origem, peca):
        raise ValueError("obter_movimento_manual: escolha invalida")


def verificar_passar_turno(tabuleiro, origem, destino, pos_jog):
    """Valida a regra de passar turno (origem == destino)."""
    if posicoes_iguais(origem, destino):
        if existe_movimento_livre(tabuleiro, pos_jog):
            raise ValueError("obter_movimento_manual: escolha invalida")
        return True
    return False


def validar_destino(tabuleiro, origem, destino):
    """Valida se o destino é livre e adjacente."""
    if not eh_posicao_livre(tabuleiro, destino):
        raise ValueError("obter_movimento_manual: escolha invalida")

    if destino not in obter_posicoes_adjacentes(origem):
        raise ValueError("obter_movimento_manual: escolha invalida")


# ==========================================================
#   MOVIMENTO AUTOMÁTICO
# ==========================================================

def obter_movimento_auto(tabuleiro, peca, nivel):
    """
    Obtém o movimento automático para o jogador indicado, com base no nível de dificuldade.
    """
    if len(obter_posicoes_jogador(tabuleiro, peca)) < 3:
        return movimento_colocacao(tabuleiro, peca)
    else:
        return movimento_movimentacao(tabuleiro, peca, nivel)


# ==========================================================
#   FASE DE COLOCAÇÃO AUTOMÁTICA
# ==========================================================

def movimento_colocacao(tabuleiro, peca):
    posicoes = obter_posicoes_livres(tabuleiro)

    condicao = vitoria(tabuleiro, posicoes, peca)
    if condicao:
        return condicao

    condicao = bloqueio(tabuleiro, posicoes, peca)
    if condicao:
        return condicao

    condicao = centro(tabuleiro)
    if condicao:
        return condicao

    condicao = cantos(posicoes)
    if condicao:
        return condicao

    condicao = laterais(posicoes)
    if condicao:
        return condicao

    if posicoes:
        return (posicoes[0],)


def vitoria(tabuleiro, posicoes, peca):
    for pos in posicoes:
        t_sim = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(t_sim, peca, pos)
        if pecas_iguais(obter_ganhador(t_sim), peca):
            return (pos,)


def bloqueio(tabuleiro, posicoes, peca):
    adversario = obter_peca_adversario(peca)
    for pos in posicoes:
        t_sim = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(t_sim, adversario, pos)
        if pecas_iguais(obter_ganhador(t_sim), adversario):
            return (pos,)


def centro(tabuleiro):
    c = cria_posicao('b', '2')
    if eh_posicao_livre(tabuleiro, c):
        return (c,)


def cantos(posicoes):
    cantos = [cria_posicao(c, l) for c, l in [('a', '1'), ('a', '3'), ('c', '1'), ('c', '3')]]
    for pos in posicoes:
        if pos in cantos:
            return (pos,)


def laterais(posicoes):
    laterais = [cria_posicao(c, l) for c, l in [('a', '2'), ('b', '1'), ('b', '3'), ('c', '2')]]
    for pos in posicoes:
        if pos in laterais:
            return (pos,)


# ==========================================================
#   FASE DE MOVIMENTAÇÃO AUTOMÁTICA
# ==========================================================

def movimento_movimentacao(tabuleiro, peca, nivel):
    pos_jogador = obter_posicoes_jogador(tabuleiro, peca)
    movimentos = movimentos_possiveis(tabuleiro, pos_jogador)

    if not movimentos:
        return (pos_jogador[0], pos_jogador[0])

    if nivel == 'facil':
        return movimentos[0]
    elif nivel == 'normal':
        resultado, jogadas = minimax(tabuleiro, peca, 1, [])
        return jogadas[0] if jogadas else movimentos[0]
    elif nivel == 'dificil':
        resultado, jogadas = minimax(tabuleiro, peca, 5, [])
        return jogadas[0]


def movimentos_possiveis(tabuleiro, pos_jogador):
    movs = []
    for origem in pos_jogador:
        for destino in obter_posicoes_adjacentes(origem):
            if eh_posicao_livre(tabuleiro, destino):
                movs.append((origem, destino))
    return movs


# ==========================================================
#   MINIMAX
# ==========================================================

def minimax(tabuleiro, peca, profundidade, seq_movimentos):
    if not pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')) or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(tabuleiro)), seq_movimentos

    melhor_resultado = -2 if peca_para_inteiro(peca) == 1 else 2
    melhor_seq = seq_movimentos

    for origem in obter_posicoes_jogador(tabuleiro, peca):
        for destino in obter_posicoes_adjacentes(origem):
            if eh_posicao_livre(tabuleiro, destino):
                t_sim = cria_copia_tabuleiro(tabuleiro)
                move_peca(t_sim, origem, destino)
                peca_adv = obter_peca_adversario(peca)
                novo_resultado, nova_seq = minimax(
                    t_sim, peca_adv, profundidade - 1, seq_movimentos + [(origem, destino)]
                )

                jogador_x = peca_para_inteiro(peca) == 1
                if (jogador_x and novo_resultado > melhor_resultado) or (not jogador_x and novo_resultado < melhor_resultado):
                    melhor_resultado, melhor_seq = novo_resultado, nova_seq

    return melhor_resultado, melhor_seq
