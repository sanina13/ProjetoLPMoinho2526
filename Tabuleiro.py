from Peca import Peca as pc
from Posicao import Posicao as ps


class Tabuleiro:
    """
    Classe que representa o tabuleiro do jogo.
    Internamente e uma lista de listas 3x3 com objetos do tipo peca.
    """

    
    # 1) CONSTRUTORES
    def __init__(self):
        """
        Cria um novo tabuleiro vazio (3x3) com peças livres (' ').
        """
        self.tabuleiro = []
        for _ in range(3):
            linha = [pc(' ') for _ in range(3)]
            self.tabuleiro.append(linha)

    # metodos estaticos apenas o  cria_tabuleiro e copia são estaticos por enquanto
    @staticmethod
    def cria_tabuleiro():
        """
        Cria e retorna um novo objeto Tabuleiro vazio (3x3) com peças livres (' ').
        """
        return Tabuleiro()
        

    @staticmethod
    def cria_copia_tabuleiro(t):
        """
        Cria uma copia independente do tabuleiro recebido.
        """
        copia = Tabuleiro()
        for linha in range(3):
            for coluna in range(3):
                copia.tabuleiro[linha][coluna] = pc.cria_copia_peca(t.tabuleiro[linha][coluna])
        return copia

    
    # 2) SELETORES E MODIFICADORES
    
    def obter_peca(self, pos):
        """
        Devolve a peca existente na posicao indicada.
        pos: objeto Posicao
        """
        col = ord(ps.obter_pos_c(pos)) - ord('a')
        lin = int(ps.obter_pos_l(pos)) - 1
        return self.tabuleiro[lin][col]


    def coloca_peca(self, j, pos):
        """
        Coloca a peca j na posicao pos.
        Altera o tabuleiro destrutivamente.
        """
        col = ord(ps.obter_pos_c(pos)) - ord('a')
        lin = int(ps.obter_pos_l(pos)) - 1
        self.tabuleiro[lin][col] = j   


    def remove_peca(self, pos):
        """
        Remove a peca de uma posicao (substitui por peca livre).
        """
        col = ord(ps.obter_pos_c(pos)) - ord('a')
        lin = int(ps.obter_pos_l(pos)) - 1
        self.tabuleiro[lin][col] = pc(' ')
        

    def move_peca(self, pos1, pos2):
        """
        Move a peca da posicao pos1 para pos2.
        """
        p = self.obter_peca(pos1)
        self.remove_peca(pos1)
        self.coloca_peca(p, pos2)

    def obter_vetor(self, s):
        """
        obter_vetor: tabuleiro × str → tuplo de pecas
        Devolve todas as peças da linha (se s ∈ {'1','2','3'}) ou
        da coluna (se s ∈ {'a','b','c'}) especificada por s.
        Lança ValueError se s for inválido.
        """
        if s in ('1', '2', '3'):
            # devolve a linha correspondente
            lin = int(s) - 1
            return tuple(self[lin][j] for j in range(3))
        elif s in ('a', 'b', 'c'):
            # devolve a coluna correspondente
            col = ord(s) - ord('a')
            return tuple(self[i][col] for i in range(3))
        else:
            raise ValueError("obter_vetor: argumento invalido")

    
