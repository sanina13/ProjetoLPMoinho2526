"""
Módulo: tabuleiro
O TAD tabuleiro representa um tabuleiro do jogo do moinho (3x3) e as peças nele colocadas.
Cada posição pode estar ocupada por uma peça ('X', 'O' ou ' ') ou livre.
"""

from models.peca import *
from models.posicao import *

# ============================================================
# Representação interna: lista de listas 3x3 de peças ('X','O',' ')
# ============================================================

LETTERS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')
TAM = 3


# ================================
#   CONSTRUTORES
# ================================

def cria_tabuleiro():
    """cria_tabuleiro: {} → tabuleiro
    Cria e devolve um tabuleiro vazio (3x3) com peças livres.
    """
    return [[cria_peca(' ') for _ in range(TAM)] for _ in range(TAM)]


def cria_copia_tabuleiro(t):
    """cria_copia_tabuleiro: tabuleiro → tabuleiro
    Devolve uma cópia independente do tabuleiro.
    """
    return [[cria_copia_peca(t[i][j]) for j in range(TAM)] for i in range(TAM)]


# ================================
#   SELETORES
# ================================

def obter_peca(t, p):
    """obter_peca: tabuleiro × posicao → peca
    Devolve a peça na posição indicada.
    """
    c = ord(obter_pos_c(p)) - ord('a')
    l = int(obter_pos_l(p)) - 1
    return t[l][c]


def obter_vetor(t, s):
    """obter_vetor: tabuleiro × str → tuplo de pecas
    Devolve todas as peças da linha (1–3) ou coluna (a–c).
    """
    if not eh_tabuleiro(t):
        raise ValueError("obter_vetor: argumento invalido")

    if s in NUMS:
        l = int(s) - 1
        return tuple(t[l][j] for j in range(TAM))
    elif s in LETTERS:
        c = ord(s) - ord('a')
        return tuple(t[i][c] for i in range(TAM))
    else:
        raise ValueError("obter_vetor: argumento invalido")


# ================================
#   MODIFICADORES (destrutivos)
# ================================

def coloca_peca(t, j, p):
    """coloca_peca: tabuleiro × peca × posicao → tabuleiro
    Coloca a peça j na posição p (modifica destrutivamente).
    """
    c = ord(obter_pos_c(p)) - ord('a')
    l = int(obter_pos_l(p)) - 1
    t[l][c] = j
    return t


def remove_peca(t, p):
    """remove_peca: tabuleiro × posicao → tabuleiro
    Remove a peça da posição p (coloca peça livre).
    """
    return coloca_peca(t, cria_peca(' '), p)


def move_peca(t, p1, p2):
    """move_peca: tabuleiro × posicao × posicao → tabuleiro
    Move a peça de p1 para p2 (modifica destrutivamente).
    """
    j = obter_peca(t, p1)
    remove_peca(t, p1)
    coloca_peca(t, j, p2)
    return t


# ================================
#   RECONHECEDORES E TESTES
# ================================

def eh_tabuleiro(arg):
    """eh_tabuleiro: universal → booleano
    Verifica se o argumento é um tabuleiro válido (3x3 e com peças válidas).
    """
    try:
        if len(arg) != TAM:
            return False
        
        for linha in arg:
            if len(linha) != TAM:
                return False
            for p in linha:
                if not eh_peca(p):
                    return False

        return True
    except Exception:
        # se não for indexável ou não tiver len(), não é um tabuleiro
        return False


def eh_posicao_livre(t, p):
    """eh_posicao_livre: tabuleiro × posicao → booleano"""
    return obter_peca(t, p) == ' '


def tabuleiros_iguais(t1, t2):
    """tabuleiros_iguais: tabuleiro × tabuleiro → booleano"""
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


# ================================
#   TRANSFORMADORES
# ================================

def tabuleiro_para_str(t):
    """tabuleiro_para_str: tabuleiro → str
    Devolve uma representação visual do tabuleiro.
    """
    linhas = ["   a   b   c"]
    for i in range(TAM):
        linha = f"{i+1} " + "-".join(peca_para_str(t[i][j]) for j in range(TAM))
        linhas.append(linha)
        if i < TAM - 1:
            linhas.append("   | \\ | / |" if i % 2 == 0 else "   | / | \\ |")
    return "\n".join(linhas)


def tuplo_para_tabuleiro(tp):
    """tuplo_para_tabuleiro: tuplo → tabuleiro
    Constrói um tabuleiro a partir de um tuplo de 3 tuplos com valores (1, -1, 0).
    """
    t = cria_tabuleiro()
    for i in range(TAM):
        for j in range(TAM):
            if tp[i][j] == 1:
                t[i][j] = 'X'
            elif tp[i][j] == -1:
                t[i][j] = 'O'
            else:
                t[i][j] = ' '
    return t


# ================================
#   FUNÇÕES DE ALTO NÍVEL
# ================================

def obter_ganhador(t):
    """obter_ganhador: tabuleiro → peca
    Devolve a peça do jogador que ganhou (3 em linha), ou uma peça livre se não há ganhador.
    """
    # Linhas
    for i in range(TAM):
        if t[i][0] == t[i][1] == t[i][2] != ' ':
            return t[i][0]
    # Colunas
    for j in range(TAM):
        if t[0][j] == t[1][j] == t[2][j] != ' ':
            return t[0][j]
    return cria_peca(' ')


def obter_posicoes_livres(t):
    """obter_posicoes_livres: tabuleiro → tuplo de posicoes"""
    livres = []
    for i in range(TAM):
        for j in range(TAM):
            if t[i][j] == ' ':
                livres.append(cria_posicao(chr(ord('a') + j), str(i + 1)))
    return tuple(livres)


def obter_posicoes_jogador(t, j):
    """obter_posicoes_jogador: tabuleiro × peca → tuplo de posicoes"""
    pos = []
    for i in range(TAM):
        for k in range(TAM):
            if pecas_iguais(t[i][k], j):
                pos.append(cria_posicao(chr(ord('a') + k), str(i + 1)))
    return tuple(pos)
