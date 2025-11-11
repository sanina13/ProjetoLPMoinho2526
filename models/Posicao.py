"""
Módulo: posicao
O TAD posicao é usado para representar uma posição do tabuleiro de jogo. Cada posição é
caraterizada pela coluna e linha que ocupa no tabuleiro. 
"""
"""
Constantes
"""
# Módulo: posicao
# TAD posicao — representa uma posição no tabuleiro de jogo (coluna, linha)

# Constantes
LETRAS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')


# ================================
#   CONSTRUTORES
# ================================

def cria_posicao(c, l):
    """cria_posicao: str × str → posicao
    Cria uma posição (tuplo) a partir da coluna c e linha l.
    """
    if c not in LETRAS or l not in NUMS:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (c, l)


def cria_copia_posicao(p):
    """cria_copia_posicao: posicao → posicao"""
    return (p[0], p[1])


# ================================
#   SELETORES
# ================================

def obter_pos_c(p):
    """obter_pos_c: posicao → str"""
    return p[0]


def obter_pos_l(p):
    """obter_pos_l: posicao → str"""
    return p[1]


# ================================
#   RECONHECEDOR
# ================================

def eh_posicao(arg):
    """eh_posicao: universal → booleano"""
    try:
        # tentar aceder como se fosse tuplo/lista
        c, l = arg[0], arg[1]
        return len(arg) == 2 and c in LETRAS and l in NUMS
    except Exception:
        return False


# ================================
#   TESTE
# ================================

def posicoes_iguais(p1, p2):
    """posicoes_iguais: posicao × posicao → booleano"""
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


# ================================
#   TRANSFORMADOR
# ================================

def posicao_para_str(p):
    """posicao_para_str: posicao → str"""
    return p[0] + p[1]


# ================================
#   FUNÇÃO DE ALTO NÍVEL
# ================================

def obter_posicoes_adjacentes(p):
    """obter_posicoes_adjacentes: posicao → tuplo de posicoes"""
    c, l = p
    adjacentes = []

    col_num = ord(c) - ord('a') + 1
    lin_num = int(l)

    # ordem: cima, esquerda, direita, baixo
    deslocamentos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    for dc, dl in deslocamentos:
        nova_c = col_num + dc
        nova_l = lin_num + dl
        if 1 <= nova_c <= 3 and 1 <= nova_l <= 3:
            adjacentes.append(cria_posicao(chr(ord('a') + nova_c - 1), str(nova_l)))

    return tuple(adjacentes)


    
