"""
Modulo: tabuleiro
O TAD tabuleiro representa um tabuleiro do jogo do moinho (3x3) e as pecas nele colocadas.
Cada posicao pode estar ocupada por uma peca ('X', 'O' ou ' ') ou livre.
"""

from models.Peca import *
from models.Posicao import *

# Representacao interna: lista de listas 3x3 de pecas ('X','O',' ')

LETTERS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')
TAM = 3


# =====================================================
# CONSTRUTORES
# =====================================================

def cria_tabuleiro():
    """cria_tabuleiro: {} -> tabuleiro"""
    return [[cria_peca(' ') for _ in range(TAM)] for _ in range(TAM)]


def cria_copia_tabuleiro(tabuleiro):
    """cria_copia_tabuleiro: tabuleiro -> tabuleiro"""
    return [[cria_copia_peca(tabuleiro[i][j]) for j in range(TAM)] for i in range(TAM)]


# =====================================================
# SELETORES
# =====================================================

def obter_peca(tabuleiro, posicao):
    """obter_peca: tabuleiro x posicao -> peca"""
    col = ord(obter_pos_c(posicao)) - ord('a')
    lin = int(obter_pos_l(posicao)) - 1
    return tabuleiro[lin][col]


def obter_vetor(tabuleiro, seletor):
    """obter_vetor: tabuleiro x str -> tuplo de pecas"""
    if seletor in NUMS:
        lin = int(seletor) - 1
        return tuple(tabuleiro[lin][j] for j in range(TAM))
    elif seletor in LETTERS:
        col = ord(seletor) - ord('a')
        return tuple(tabuleiro[i][col] for i in range(TAM))
    else:
        raise ValueError("obter_vetor: argumento invalido")


# =====================================================
# MODIFICADORES (destrutivos)
# =====================================================

def coloca_peca(tabuleiro, peca, posicao):
    """coloca_peca: tabuleiro x peca x posicao -> tabuleiro"""
    col = ord(obter_pos_c(posicao)) - ord('a')
    lin = int(obter_pos_l(posicao)) - 1
    tabuleiro[lin][col] = peca
    return tabuleiro


def remove_peca(tabuleiro, posicao):
    """remove_peca: tabuleiro x posicao -> tabuleiro"""
    return coloca_peca(tabuleiro, cria_peca(' '), posicao)


def move_peca(tabuleiro, pos_origem, pos_destino):
    """move_peca: tabuleiro x posicao x posicao -> tabuleiro"""
    p = obter_peca(tabuleiro, pos_origem)
    remove_peca(tabuleiro, pos_origem)
    coloca_peca(tabuleiro, p, pos_destino)
    return tabuleiro


# =====================================================
# RECONHECEDORES E TESTES
# =====================================================

def eh_tabuleiro(tabuleiro):
    """eh_tabuleiro: universal -> booleano"""
    try:
        if len(tabuleiro) != TAM:
            return False

        countX = countO = 0

        for linha in tabuleiro:
            if len(linha) != TAM:
                return False
            for p in linha:
                if not eh_peca(p):
                    return False
                if p == cria_peca('X'):
                    countX += 1
                elif p == cria_peca('O'):
                    countO += 1

        if countX > 3 or countO > 3:
            return False
        if abs(countX - countO) > 1:
            return False
        if contar_vencedores(tabuleiro) > 1:
            return False

        return True
    except Exception:
        return False


def eh_posicao_livre(tabuleiro, posicao):
    """eh_posicao_livre: tabuleiro x posicao -> booleano"""
    return obter_peca(tabuleiro, posicao) == cria_peca(' ')


def tabuleiros_iguais(t1, t2):
    """tabuleiros_iguais: tabuleiro x tabuleiro -> booleano"""
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


# =====================================================
# TRANSFORMADORES
# =====================================================

def tabuleiro_para_str(tabuleiro):
    """tabuleiro_para_str: tabuleiro -> str"""
    linhas = ["   a   b   c"]

    linhas.append("1 " + "-".join(peca_para_str(tabuleiro[0][j]) for j in range(TAM)))
    linhas.append("   | \\ | / |")

    linhas.append("2 " + "-".join(peca_para_str(tabuleiro[1][j]) for j in range(TAM)))
    linhas.append("   | / | \\ |")

    linhas.append("3 " + "-".join(peca_para_str(tabuleiro[2][j]) for j in range(TAM)))

    return "\n".join(linhas)


def tuplo_para_tabuleiro(t):
    """tuplo_para_tabuleiro: tuplo -> tabuleiro"""
    tab = cria_tabuleiro()
    for i in range(TAM):
        for j in range(TAM):
            if t[i][j] == 1:
                tab[i][j] = cria_peca('X')
            elif t[i][j] == -1:
                tab[i][j] = cria_peca('O')
            else:
                tab[i][j] = cria_peca(' ')
    return tab


# =====================================================
# FUNCOES DE ALTO NIVEL
# =====================================================

def obter_ganhador(tabuleiro):
    """obter_ganhador: tabuleiro -> peca"""

    # Linhas
    for i in range(TAM):
        p1 = obter_peca(tabuleiro, cria_posicao('a', str(i + 1)))
        p2 = obter_peca(tabuleiro, cria_posicao('b', str(i + 1)))
        p3 = obter_peca(tabuleiro, cria_posicao('c', str(i + 1)))
        if p1 == p2 == p3 != cria_peca(' '):
            return p1

    # Colunas
    for j in range(TAM):
        col = chr(ord('a') + j)
        p1 = obter_peca(tabuleiro, cria_posicao(col, '1'))
        p2 = obter_peca(tabuleiro, cria_posicao(col, '2'))
        p3 = obter_peca(tabuleiro, cria_posicao(col, '3'))
        if p1 == p2 == p3 != cria_peca(' '):
            return p1

    return cria_peca(' ')


def obter_posicoes_livres(tabuleiro):
    """obter_posicoes_livres: tabuleiro -> tuplo de posicoes"""
    livres = []
    for i in range(TAM):
        for j in range(TAM):
            pos = cria_posicao(chr(ord('a') + j), str(i + 1))
            if eh_posicao_livre(tabuleiro, pos):
                livres.append(pos)
    return tuple(livres)


def obter_posicoes_jogador(tabuleiro, peca):
    """obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes"""
    res = []
    for i in range(TAM):
        for j in range(TAM):
            pos = cria_posicao(chr(ord('a') + j), str(i + 1))
            if pecas_iguais(obter_peca(tabuleiro, pos), peca):
                res.append(pos)
    return tuple(res)


# =====================================================
# FUNCAO AUXILIAR
# =====================================================

def contar_vencedores(tabuleiro):
    """contar_vencedores: tabuleiro -> int"""
    count = 0

    # Linhas
    for i in range(TAM):
        p1 = obter_peca(tabuleiro, cria_posicao('a', str(i + 1)))
        p2 = obter_peca(tabuleiro, cria_posicao('b', str(i + 1)))
        p3 = obter_peca(tabuleiro, cria_posicao('c', str(i + 1)))
        if p1 == p2 == p3 != cria_peca(' '):
            count += 1

    # Colunas
    for j in range(TAM):
        col = chr(ord('a') + j)
        p1 = obter_peca(tabuleiro, cria_posicao(col, '1'))
        p2 = obter_peca(tabuleiro, cria_posicao(col, '2'))
        p3 = obter_peca(tabuleiro, cria_posicao(col, '3'))
        if p1 == p2 == p3 != cria_peca(' '):
            count += 1

    return count
