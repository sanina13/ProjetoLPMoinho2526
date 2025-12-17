"""
Modulo: posicao
O TAD posicao e usado para representar uma posicao do tabuleiro de jogo.
Cada posicao e caracterizada pela coluna e linha que ocupa no tabuleiro.
"""

# Constantes
LETRAS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')


# =====================================================
# CONSTRUTORES
# =====================================================

def cria_posicao(coluna, linha):
    """cria_posicao: str x str -> posicao"""
    if coluna not in LETRAS or linha not in NUMS:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (coluna, linha)


def cria_copia_posicao(posicao):
    """cria_copia_posicao: posicao -> posicao"""
    return cria_posicao(obter_pos_c(posicao), obter_pos_l(posicao))


# =====================================================
# SELETORES
# =====================================================

def obter_pos_c(posicao):
    """obter_pos_c: posicao -> str"""
    return posicao[0]


def obter_pos_l(posicao):
    """obter_pos_l: posicao -> str"""
    return posicao[1]


# =====================================================
# RECONHECEDOR
# =====================================================

def eh_posicao(arg):
    """eh_posicao: universal -> booleano"""
    try:
        return (
            isinstance(arg, tuple) and
            len(arg) == 2 and
            arg[0] in LETRAS and
            arg[1] in NUMS
        )
    except Exception:
        return False


# =====================================================
# TESTE
# =====================================================

def posicoes_iguais(p1, p2):
    """posicoes_iguais: posicao x posicao -> booleano"""
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


# =====================================================
# TRANSFORMADOR
# =====================================================

def posicao_para_str(posicao):
    """posicao_para_str: posicao -> str"""
    return obter_pos_c(posicao) + obter_pos_l(posicao)


# =====================================================
# FUNCAO DE ALTO NIVEL
# =====================================================

def obter_posicoes_adjacentes(posicao):
    """obter_posicoes_adjacentes: posicao -> tuplo de posicoes"""
    col = ord(obter_pos_c(posicao)) - ord('a')
    lin = int(obter_pos_l(posicao)) - 1

    adj = []

    for dl in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dl == 0 and dc == 0:
                continue

            nl = lin + dl
            nc = col + dc

            if 0 <= nl < 3 and 0 <= nc < 3:
                # diagonais so nos centros e cantos
                if dl != 0 and dc != 0:
                    if not (lin == col or lin + col == 2):
                        continue

                adj.append(
                    cria_posicao(chr(ord('a') + nc), str(nl + 1))
                )

    # ordem de leitura do tabuleiro
    adj.sort(key=lambda p: (int(obter_pos_l(p)), obter_pos_c(p)))
    return tuple(adj)
