"""
Módulo: peca
O TAD peca é usado para representar as peças do jogo do moinho.
Cada peça é caracterizada pelo jogador ('X', 'O') ou pode ser livre (' ').
"""

# ============================================================
#   Representação interna: string simples ('X', 'O' ou ' ')
# ============================================================

PECAS_VALIDAS = ('X', 'O', ' ')

# ================================
#   CONSTRUTORES
# ================================

def cria_peca(s):
    """cria_peca: str → peca
    Cria uma peça correspondente ao jogador indicado ('X', 'O' ou ' ').
    """
    if s not in PECAS_VALIDAS:
        raise ValueError("cria_peca: argumento invalido")
    return s


def cria_copia_peca(j):
    """cria_copia_peca: peca → peca
    Devolve uma cópia da peça.
    """
    if not eh_peca(j):
        raise ValueError("cria_copia_peca: argumento invalido")
    
    return j


# ================================
#   RECONHECEDOR
# ================================

def eh_peca(arg):
    """eh_peca: universal → booleano
    Devolve True se o argumento representar uma peça válida ('X', 'O' ou ' ').
    """
    try:
        return len(arg) == 1 and arg in PECAS_VALIDAS
    except Exception:
        return False



# ================================
#   TESTE
# ================================

def pecas_iguais(j1, j2):
    """pecas_iguais: peca × peca → booleano
    Devolve True apenas se j1 e j2 são peças e são iguais.
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2


# ================================
#   TRANSFORMADORES
# ================================

def peca_para_str(j):
    """peca_para_str: peca → str
    Devolve a cadeia '[X]', '[O]' ou '[ ]' que representa a peça.
    """
    return f"[{j}]"


def peca_para_inteiro(j):
    """peca_para_inteiro: peca → int
    Devolve:
      1 se a peça é 'X'
     -1 se a peça é 'O'
      0 se a peça é ' ' (livre)
    """
    if j == 'X':
        return 1
    elif j == 'O':
        return -1
    else:
        return 0


# ================================
#   FUNÇÃO AUXILIAR (não obrigatória)
# ================================

def obter_peca_adversario(j):
    """obter_peca_adversario: peca → peca
    Devolve a peça do jogador adversário.
    """
    if j == 'X':
        return 'O'
    elif j == 'O':
        return 'X'
    else:
        return ' '  # livre não tem adversário
