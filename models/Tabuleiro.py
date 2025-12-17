"""
Módulo: tabuleiro
O TAD tabuleiro representa um tabuleiro do jogo do moinho (3x3) e as peças nele colocadas.
Cada posição pode estar ocupada por uma peça ('X', 'O' ou ' ') ou livre.
"""

from models.Peca import *
from models.Posicao import *

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


def cria_copia_tabuleiro(tabuleiro):
    """cria_copia_tabuleiro: tabuleiro → tabuleiro
    Devolve uma cópia independente do tabuleiro.
    """
    return [[cria_copia_peca(tabuleiro[i][j]) for j in range(TAM)] for i in range(TAM)]


# ================================
#   SELETORES
# ================================

def obter_peca(tabuleiro, posicao):
    """obter_peca: tabuleiro × posicao → peca
    Devolve a peça na posição indicada.
    """
    coluna_indice = ord(obter_pos_c(posicao)) - ord('a')
    linha_indice = int(obter_pos_l(posicao)) - 1
    return tabuleiro[linha_indice][coluna_indice]


def obter_vetor(tabuleiro, seletor):
    """obter_vetor: tabuleiro × str → tuplo de pecas
    Devolve todas as peças da linha (1–3) ou coluna (a–c).
    """
    if not eh_tabuleiro(tabuleiro):
        raise ValueError("obter_vetor: argumento invalido")

    if seletor in NUMS:
        linha_indice = int(seletor) - 1
        return tuple(tabuleiro[linha_indice][j] for j in range(TAM))
    elif seletor in LETTERS:
        coluna_indice = ord(seletor) - ord('a')
        return tuple(tabuleiro[i][coluna_indice] for i in range(TAM))
    else:
        raise ValueError("obter_vetor: argumento invalido")


# ================================
#   MODIFICADORES (destrutivos)
# ================================

def coloca_peca(tabuleiro, peca, posicao):
    """coloca_peca: tabuleiro × peca × posicao → tabuleiro
    Coloca a peça j na posição p (modifica destrutivamente).
    """
    coluna_indice = ord(obter_pos_c(posicao)) - ord('a')
    linha_indice = int(obter_pos_l(posicao)) - 1
    tabuleiro[linha_indice][coluna_indice] = peca
    return tabuleiro


def remove_peca(tabuleiro, posicao):
    """remove_peca: tabuleiro × posicao → tabuleiro
    Remove a peça da posição p (coloca peça livre).
    """
    return coloca_peca(tabuleiro, cria_peca(' '), posicao)


def move_peca(tabuleiro, posicao_origem, posicao_destino):
    """move_peca: tabuleiro × posicao × posicao → tabuleiro
    Move a peça de p1 para p2 (modifica destrutivamente).
    """
    peca_origem = obter_peca(tabuleiro, posicao_origem)
    remove_peca(tabuleiro, posicao_origem)
    coloca_peca(tabuleiro, peca_origem, posicao_destino)
    return tabuleiro


# ================================
#   RECONHECEDORES E TESTES
# ================================

def eh_tabuleiro(argumento):
    """eh_tabuleiro: universal → booleano
    Verifica se o argumento é um tabuleiro válido (3x3 e com peças válidas).
    """
    try:
        if len(argumento) != TAM:
            return False
        
        for linha in argumento:
            if len(linha) != TAM:
                return False
            for peca in linha:
                if not eh_peca(peca):
                    return False

        return True
    except Exception:
        # se não for indexável ou não tiver len(), não é um tabuleiro
        return False


def eh_posicao_livre(tabuleiro, posicao):
    """eh_posicao_livre: tabuleiro × posicao → booleano"""
    return obter_peca(tabuleiro, posicao) == cria_peca(' ')


def tabuleiros_iguais(tabuleiro1, tabuleiro2):
    """tabuleiros_iguais: tabuleiro × tabuleiro → booleano"""
    return eh_tabuleiro(tabuleiro1) and eh_tabuleiro(tabuleiro2) and tabuleiro1 == tabuleiro2


# ================================
#   TRANSFORMADORES
# ================================

def tabuleiro_para_str(tabuleiro):
    """tabuleiro_para_str: tabuleiro → str
    Devolve uma representação visual do tabuleiro.
    """
    linhas = ["   a   b   c"]
    for i in range(TAM):
        linha = f"{i+1} " + "-".join(peca_para_str(tabuleiro[i][j]) for j in range(TAM))
        linhas.append(linha)
        if i < TAM - 1:
            linhas.append("   | \\ | / |" if i % 2 == 0 else "   | / | \\ |")
    return "\n".join(linhas)


def tuplo_para_tabuleiro(tuplo_tabuleiro):
    """tuplo_para_tabuleiro: tuplo → tabuleiro
    Constrói um tabuleiro a partir de um tuplo de 3 tuplos com valores (1, -1, 0).
    """
    tabuleiro = cria_tabuleiro()
    for i in range(TAM):
        for j in range(TAM):
            if tuplo_tabuleiro[i][j] == 1:
                tabuleiro[i][j] = cria_peca('X')
            elif tuplo_tabuleiro[i][j] == -1:
                tabuleiro[i][j] = cria_peca('O')
            else:
                tabuleiro[i][j] = cria_peca(' ')
    return tabuleiro


# ================================
#   FUNÇÕES DE ALTO NÍVEL
# ================================

def obter_ganhador(tabuleiro):
    """obter_ganhador: tabuleiro → peca
    Devolve a peça do jogador que ganhou (3 em linha), ou uma peça livre se não há ganhador.
    """
    # Linhas
    for i in range(TAM):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != cria_peca(' '):
            return tabuleiro[i][0]
    # Colunas
    for j in range(TAM):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != cria_peca(' '):
            return tabuleiro[0][j]
    return cria_peca(' ')


def obter_posicoes_livres(tabuleiro):
    """obter_posicoes_livres: tabuleiro → tuplo de posicoes"""
    livres = []
    for i in range(TAM):
        for j in range(TAM):
            if tabuleiro[i][j] == ' ':
                livres.append(cria_posicao(chr(ord('a') + j), str(i + 1)))
    return tuple(livres)


def obter_posicoes_jogador(tabuleiro, peca):
    """obter_posicoes_jogador: tabuleiro × peca → tuplo de posicoes"""
    posicoes = []
    for i in range(TAM):
        for k in range(TAM):
            if pecas_iguais(tabuleiro[i][k], peca):
                posicoes.append(cria_posicao(chr(ord('a') + k), str(i + 1)))
    return tuple(posicoes)
