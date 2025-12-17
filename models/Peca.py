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
    """cria_peca: str -> peca"""
    if s not in PECAS_VALIDAS:
        raise ValueError("cria_peca: argumento invalido")
    return s


def cria_copia_peca(peca):
    """cria_copia_peca: peca -> peca"""
    return peca


# =====================================================
# RECONHECEDOR
# =====================================================

def eh_peca(arg):
    """eh_peca: universal -> booleano"""
    return arg in PECAS_VALIDAS


# =====================================================
# TESTE
# =====================================================

def pecas_iguais(j1, j2):
    """pecas_iguais: peca x peca -> booleano"""
    return eh_peca(j1) and eh_peca(j2) and j1 == j2


# =====================================================
# TRANSFORMADOR
# =====================================================

def peca_para_str(peca):
    """peca_para_str: peca -> str"""
    return "[" + peca + "]"


# =====================================================
# FUNCAO DE ALTO NIVEL
# =====================================================

def peca_para_inteiro(peca):
    """peca_para_inteiro: peca -> int"""
    if peca == 'X':
        return 1
    if peca == 'O':
        return -1
    return 0


# =====================================================
# FUNCAO AUXILIAR (opcional)
# =====================================================

def obter_peca_adversario(peca):
    """obter_peca_adversario: peca -> peca"""
    if peca == 'X':
        return 'O'
    if peca == 'O':
        return 'X'
    return ' '
