"""
Modulo: peca
O TAD peca e usado para representar as pecas do jogo do moinho.
Cada peca pertence ao jogador 'X', 'O' ou e livre (' ').
"""

PECAS_VALIDAS = ('X', 'O', ' ')


# =====================================================
# CONSTRUTORES
# =====================================================

def cria_peca(s):
    if s not in PECAS_VALIDAS:
        raise ValueError("cria_peca: argumento invalido")
    return s


def cria_copia_peca(peca):
    return peca


# =====================================================
# RECONHECEDOR
# =====================================================

def eh_peca(arg):
    return arg in PECAS_VALIDAS


# =====================================================
# TESTE
# =====================================================

def pecas_iguais(p1, p2):
    return eh_peca(p1) and eh_peca(p2) and p1 == p2


# =====================================================
# TRANSFORMADOR
# =====================================================

def peca_para_str(peca):
    return "[" + peca + "]"


# =====================================================
# FUNCAO DE ALTO NIVEL
# =====================================================

def peca_para_inteiro(peca):
    if peca == 'X':
        return 1
    if peca == 'O':
        return -1
    return 0


# =====================================================
# FUNCAO AUXILIAR
# =====================================================

def obter_peca_adversario(peca):
    if peca == 'X':
        return 'O'
    if peca == 'O':
        return 'X'
    return ' '
