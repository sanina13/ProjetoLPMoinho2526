from peca import peca
from posicao import Posicao


class Tabuleiro:
    """
    Classe que representa o tabuleiro do jogo.
    Internamente e uma lista de listas 3x3 com objetos do tipo peca.
    """

    
    # 1) CONSTRUTORES


    @staticmethod
    def cria_tabuleiro():
        """
        Cria um novo tabuleiro vazio (3x3) com pecas livres (' ').
        Retorna: matriz 3x3 de objetos peca.
        """
        tabuleiro = []
        for _ in range(3):
            linha = [peca(' ') for _ in range(3)]
            tabuleiro.append(linha)
        return tabuleiro

    @staticmethod
    def cria_copia_tabuleiro(t):
        """
        Cria uma copia independente do tabuleiro recebido.
        """
        copia = []
        for linha in t:
            nova = [peca.cria_copia_peca(p) for p in linha]
            copia.append(nova)
        return copia

    
    # 2) SELETORES E MODIFICADORES
    
    @staticmethod
    def obter_peca(t, pos):
        """
        Devolve a peca existente na posicao indicada.
        pos: objeto Posicao
        """
        col = ord(Posicao.obter_pos_c(pos)) - ord('a')
        lin = int(Posicao.obter_pos_l(pos)) - 1
        return t[lin][col]

    @staticmethod
    def coloca_peca(t, j, pos):
        """
        Coloca a peca j na posicao pos.
        Altera o tabuleiro destrutivamente.
        """
        col = ord(Posicao.obter_pos_c(pos)) - ord('a')
        lin = int(Posicao.obter_pos_l(pos)) - 1
        t[lin][col] = j
        return t

    @staticmethod
    def remove_peca(t, pos):
        """
        Remove a peca de uma posicao (substitui por peca livre).
        """
        col = ord(Posicao.obter_pos_c(pos)) - ord('a')
        lin = int(Posicao.obter_pos_l(pos)) - 1
        t[lin][col] = peca(' ')
        return t

    @staticmethod
    def move_peca(t, pos1, pos2):
        """
        Move a peca da posicao pos1 para pos2.
        """
        p = Tabuleiro.obter_peca(t, pos1)
        Tabuleiro.remove_peca(t, pos1)
        Tabuleiro.coloca_peca(t, p, pos2)
        return t

    