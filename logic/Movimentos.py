from models.Tabuleiro import *


# =====================================================
# MOVIMENTO (MANUAL OU AUTOMATICO)
# =====================================================

def obter_movimento(tabuleiro, peca, nivel=None):
    if nivel is None:
        return obter_movimento_manual(tabuleiro, peca)
    return obter_movimento_auto(tabuleiro, peca, nivel)


# =====================================================
# MOVIMENTO MANUAL
# =====================================================

def obter_movimento_manual(tabuleiro, peca):
    posicoes_jogador = obter_posicoes_jogador(tabuleiro, peca)

    # ---------------- FASE DE COLOCACAO ----------------
    if len(posicoes_jogador) < 3:
        entrada = input("Turno do jogador. Escolha uma posicao: ")

        if len(entrada) != 2:
            raise ValueError("obter_movimento_manual: escolha invalida")

        pos = cria_posicao(entrada[0], entrada[1])

        if not eh_posicao_livre(tabuleiro, pos):
            raise ValueError("obter_movimento_manual: escolha invalida")

        return (pos,)

    # -------------- FASE DE MOVIMENTACAO ---------------
    entrada = input("Turno do jogador. Escolha um movimento: ")

    if len(entrada) != 4:
        raise ValueError("obter_movimento_manual: escolha invalida")

    origem = cria_posicao(entrada[0], entrada[1])
    destino = cria_posicao(entrada[2], entrada[3])

    if not pecas_iguais(obter_peca(tabuleiro, origem), peca):
        raise ValueError("obter_movimento_manual: escolha invalida")

    # passar turno (origem == destino)
    if posicoes_iguais(origem, destino):
        for p in posicoes_jogador:
            for adj in obter_posicoes_adjacentes(p):
                if eh_posicao_livre(tabuleiro, adj):
                    raise ValueError("obter_movimento_manual: escolha invalida")
        return (origem, destino)

    if not eh_posicao_livre(tabuleiro, destino):
        raise ValueError("obter_movimento_manual: escolha invalida")

    if destino not in obter_posicoes_adjacentes(origem):
        raise ValueError("obter_movimento_manual: escolha invalida")

    return (origem, destino)


# =====================================================
# MOVIMENTO AUTOMATICO
# =====================================================

def obter_movimento_auto(tabuleiro, peca, nivel):
    if len(obter_posicoes_jogador(tabuleiro, peca)) < 3:
        return movimento_colocacao(tabuleiro, peca)
    return movimento_movimentacao(tabuleiro, peca, nivel)


# ---------------- FASE DE COLOCACAO -------------------

def movimento_colocacao(tabuleiro, peca):
    livres = obter_posicoes_livres(tabuleiro)

    r = vitoria(tabuleiro, livres, peca)
    if r:
        return r

    r = bloqueio(tabuleiro, livres, peca)
    if r:
        return r

    if eh_posicao_livre(tabuleiro, cria_posicao('b', '2')):
        return (cria_posicao('b', '2'),)

    for p in livres:
        if posicoes_iguais(p, cria_posicao('a', '1')) or \
           posicoes_iguais(p, cria_posicao('a', '3')) or \
           posicoes_iguais(p, cria_posicao('c', '1')) or \
           posicoes_iguais(p, cria_posicao('c', '3')):
            return (p,)

    for p in livres:
        if posicoes_iguais(p, cria_posicao('a', '2')) or \
           posicoes_iguais(p, cria_posicao('b', '1')) or \
           posicoes_iguais(p, cria_posicao('b', '3')) or \
           posicoes_iguais(p, cria_posicao('c', '2')):
            return (p,)

    return (livres[0],)


def vitoria(tabuleiro, livres, peca):
    for p in livres:
        t = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(t, peca, p)
        if pecas_iguais(obter_ganhador(t), peca):
            return (p,)


def bloqueio(tabuleiro, livres, peca):
    adv = obter_peca_adversario(peca)
    for p in livres:
        t = cria_copia_tabuleiro(tabuleiro)
        coloca_peca(t, adv, p)
        if pecas_iguais(obter_ganhador(t), adv):
            return (p,)


# -------------- FASE DE MOVIMENTACAO ------------------

def movimento_movimentacao(tabuleiro, peca, nivel):
    posicoes = obter_posicoes_jogador(tabuleiro, peca)
    movimentos = movimentos_possiveis(tabuleiro, posicoes)

    if not movimentos:
        return (posicoes[0], posicoes[0])

    if nivel == 'facil':
        return movimentos[0]

    profundidade = 1 if nivel == 'normal' else 5
    _, seq = minimax(tabuleiro, peca, profundidade)

    return seq[0] if seq else movimentos[0]


def movimentos_possiveis(tabuleiro, posicoes):
    movs = []
    for o in posicoes:
        for d in obter_posicoes_adjacentes(o):
            if eh_posicao_livre(tabuleiro, d):
                movs.append((o, d))
    return movs


# =====================================================
# MINIMAX
# =====================================================

def minimax(tabuleiro, peca, profundidade):
    if not pecas_iguais(obter_ganhador(tabuleiro), cria_peca(' ')) or profundidade == 0:
        return peca_para_inteiro(obter_ganhador(tabuleiro)), []

    melhor = -2 if peca_para_inteiro(peca) == 1 else 2
    melhor_seq = []

    posicoes = sorted(
        obter_posicoes_jogador(tabuleiro, peca),
        key=lambda p: (int(obter_pos_l(p)), obter_pos_c(p))
    )

    for origem in posicoes:
        destinos = sorted(
            obter_posicoes_adjacentes(origem),
            key=lambda p: (int(obter_pos_l(p)), obter_pos_c(p))
        )

        for destino in destinos:
            if eh_posicao_livre(tabuleiro, destino):
                t = cria_copia_tabuleiro(tabuleiro)
                move_peca(t, origem, destino)

                resultado, _ = minimax(
                    t,
                    obter_peca_adversario(peca),
                    profundidade - 1
                )

                if (peca_para_inteiro(peca) == 1 and resultado > melhor) or \
                   (peca_para_inteiro(peca) == -1 and resultado < melhor):
                    melhor = resultado
                    melhor_seq = [(origem, destino)]

    return melhor, melhor_seq
