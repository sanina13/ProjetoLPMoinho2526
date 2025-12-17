from models.Peca import *
from models.Posicao import *

LETTERS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')
TAM = 3


# =====================================================
# CONSTRUTORES
# =====================================================

def cria_tabuleiro():
    return [[cria_peca(' ') for _ in range(TAM)] for _ in range(TAM)]


def cria_copia_tabuleiro(tab):
    return [[cria_copia_peca(tab[i][j]) for j in range(TAM)] for i in range(TAM)]


# =====================================================
# SELETORES
# =====================================================

def obter_peca(tab, pos):
    col = ord(obter_pos_c(pos)) - ord('a')
    lin = int(obter_pos_l(pos)) - 1
    return tab[lin][col]


def obter_vetor(tab, s):
    if s in NUMS:  # linha
        lin = int(s) - 1
        return tuple(tab[lin][j] for j in range(TAM))
    if s in LETTERS:  # coluna
        col = ord(s) - ord('a')
        return tuple(tab[i][col] for i in range(TAM))
    raise ValueError("obter_vetor: argumento invalido")


# =====================================================
# MODIFICADORES
# =====================================================

def coloca_peca(tab, peca, pos):
    col = ord(obter_pos_c(pos)) - ord('a')
    lin = int(obter_pos_l(pos)) - 1
    tab[lin][col] = peca
    return tab


def remove_peca(tab, pos):
    return coloca_peca(tab, cria_peca(' '), pos)


def move_peca(tab, origem, destino):
    p = obter_peca(tab, origem)
    remove_peca(tab, origem)
    coloca_peca(tab, p, destino)
    return tab


# =====================================================
# RECONHECEDORES
# =====================================================

def eh_tabuleiro(tab):
    try:
        if len(tab) != TAM:
            return False

        xs = os = 0

        for i in range(TAM):
            if len(tab[i]) != TAM:
                return False
            for p in tab[i]:
                if not eh_peca(p):
                    return False
                if pecas_iguais(p, cria_peca('X')):
                    xs += 1
                elif pecas_iguais(p, cria_peca('O')):
                    os += 1

        if xs > 3 or os > 3 or abs(xs - os) > 1:
            return False

        if contar_vencedores(tab) > 1:
            return False

        return True
    except:
        return False


def eh_posicao_livre(tab, pos):
    return pecas_iguais(obter_peca(tab, pos), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


# =====================================================
# TRANSFORMADOR
# =====================================================

def tabuleiro_para_str(tab):
    linhas = ["   a   b   c"]

    linhas.append("1 " + "-".join(peca_para_str(tab[0][j]) for j in range(TAM)))
    linhas.append("   | \\ | / |")

    linhas.append("2 " + "-".join(peca_para_str(tab[1][j]) for j in range(TAM)))
    linhas.append("   | / | \\ |")

    linhas.append("3 " + "-".join(peca_para_str(tab[2][j]) for j in range(TAM)))

    return "\n".join(linhas)


def tuplo_para_tabuleiro(t):
    tab = cria_tabuleiro()
    for i in range(TAM):
        for j in range(TAM):
            pos = cria_posicao(chr(ord('a') + j), str(i + 1))
            if t[i][j] == 1:
                coloca_peca(tab, cria_peca('X'), pos)
            elif t[i][j] == -1:
                coloca_peca(tab, cria_peca('O'), pos)
    return tab


# =====================================================
# FUNÇÕES DE ALTO NÍVEL
# =====================================================

def obter_ganhador(tab):
    for i in range(TAM):
        if (pecas_iguais(tab[i][0], tab[i][1]) and
            pecas_iguais(tab[i][1], tab[i][2]) and
            not pecas_iguais(tab[i][0], cria_peca(' '))):
            return tab[i][0]

    for j in range(TAM):
        if (pecas_iguais(tab[0][j], tab[1][j]) and
            pecas_iguais(tab[1][j], tab[2][j]) and
            not pecas_iguais(tab[0][j], cria_peca(' '))):
            return tab[0][j]

    return cria_peca(' ')


def obter_posicoes_livres(tab):
    res = []
    for i in range(TAM):
        for j in range(TAM):
            pos = cria_posicao(chr(ord('a') + j), str(i + 1))
            if eh_posicao_livre(tab, pos):
                res.append(pos)
    return tuple(res)


def obter_posicoes_jogador(tab, peca):
    res = []
    for i in range(TAM):
        for j in range(TAM):
            pos = cria_posicao(chr(ord('a') + j), str(i + 1))
            if pecas_iguais(obter_peca(tab, pos), peca):
                res.append(pos)
    return tuple(res)


# =====================================================
# AUXILIAR
# =====================================================

def contar_vencedores(tab):
    count = 0

    for i in range(TAM):
        if (pecas_iguais(tab[i][0], tab[i][1]) and
            pecas_iguais(tab[i][1], tab[i][2]) and
            not pecas_iguais(tab[i][0], cria_peca(' '))):
            count += 1

    for j in range(TAM):
        if (pecas_iguais(tab[0][j], tab[1][j]) and
            pecas_iguais(tab[1][j], tab[2][j]) and
            not pecas_iguais(tab[0][j], cria_peca(' '))):
            count += 1

    return count
