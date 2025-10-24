from models.Peca import Peca as pc
from models.Posicao import Posicao as ps

letters = ('a', 'b', 'c')
nums = ('1', '2', '3')
tamanho_tabuleiro = 3

class Tabuleiro:
    """
    Classe que representa o tabuleiro do jogo.
    Internamente e uma lista de listas tamanho_tabuleiro x tamanho_tabuleiro com objetos do tipo peca.
    """

    
    # 1) CONSTRUTORES
    def __init__(self):
        """
        Cria um novo tabuleiro vazio (tamanho_tabuleiro x tamanho_tabuleiro) com peças livres (' ').
        """
        self.tabuleiro_lista = []
        for _ in range(tamanho_tabuleiro):
            linha = [pc(' ') for _ in range(tamanho_tabuleiro)]
            self.tabuleiro_lista.append(linha)

    # metodos estaticos apenas o  cria_tabuleiro e copia são estaticos por enquanto
    @staticmethod
    def cria_tabuleiro():
        """
        Cria e retorna um novo objeto Tabuleiro vazio (tamanho_tabuleiro x tamanho_tabuleiro) com peças livres (' ').
        """
        return Tabuleiro()
        

    @staticmethod
    def cria_copia_tabuleiro(tabuleiro):
        """
        Cria uma copia independente do tabuleiro recebido.
        """
        copia = Tabuleiro()
        for linha in range(tamanho_tabuleiro):
            for coluna in range(tamanho_tabuleiro):
                copia.tabuleiro_lista[linha][coluna] = pc.cria_copia_peca(tabuleiro.tabuleiro_lista[linha][coluna])
        return copia

    
    # 2) SELETORES E MODIFICADORES
    
    def obter_peca(self, pos):
        """
        Devolve a peca existente na posicao indicada.
        pos: objeto Posicao
        """
        col = ord(ps.obter_pos_c(pos)) - ord('a')
        lin = int(ps.obter_pos_l(pos)) - 1
        return self.tabuleiro_lista[lin][col]


    def coloca_peca(self, j, pos):
        """
        Coloca a peca j na posicao pos.
        Altera o tabuleiro destrutivamente.
        """
        col = ord(pos.obter_pos_c()) - ord('a')
        lin = int(pos.obter_pos_l()) - 1
        self.tabuleiro_lista[lin][col] = j
        return self


    def remove_peca(self, pos):
        """
        Remove a peca de uma posicao (substitui por peca livre).
        """
        col = ord(ps.obter_pos_c(pos)) - ord('a')
        lin = int(ps.obter_pos_l(pos)) - 1
        self.tabuleiro_lista[lin][col] = pc(' ')
        return self

    def move_peca(self, pos1, pos2):
        """
        Move a peca da posicao pos1 para pos2.
        """
        p = self.obter_peca(pos1)
        self.remove_peca(pos1)
        self.coloca_peca(p, pos2)
        return self

    
    
    def obter_vetor(self, s):
        """
        obter_vetor: tabuleiro × str → tuplo de pecas
        Devolve todas as peças da linha (se s ∈ {'1','2','3'}) ou
        da coluna (se s ∈ {'a','b','c'}) especificada por s.
        Lança ValueError se s for inválido.
        """
        if not Tabuleiro.eh_tabuleiro(self):
            raise ValueError("obter_vetor: argumento invalido")
        board = self.tabuleiro_lista

        if s in nums:
            # devolve a linha correspondente
            lin = int(s) - 1
            return tuple(board[lin][j] for j in range(tamanho_tabuleiro))
        elif s in letters:
            # devolve a coluna correspondente
            col = ord(s) - ord('a')
            return tuple(board[i][col] for i in range(tamanho_tabuleiro))
        else:
            raise ValueError("obter_vetor: argumento invalido")
        
    # ==============================
    # 3) RECONHECEDORES E TESTES
    # ==============================
    def eh_tabuleiro(arg):
        if not type(arg) == Tabuleiro:
            return False
        try:
            tabuleiro = arg.tabuleiro_lista
            if not type(tabuleiro) == list or len(tabuleiro) != tamanho_tabuleiro:
                return False
            for linha in tabuleiro:
                if not type(linha) == list or len(linha) != tamanho_tabuleiro:
                    return False
                for p in linha:
                    if not pc.eh_peca(p):
                        return False
            return True
        except AttributeError:
            return False

    def eh_posicao_livre(self, pos):
        return self.obter_peca(pos).player == ' '

    @staticmethod 
    def tabuleiros_iguais(t1, t2): 
        return t1.tabuleiro_lista == t2.tabuleiro_lista

    # ==============================
    # 4) TRANSFORMADORES
    # ==============================

    def cabecalho(self):
        cabecalho = ""
        for i in range(tamanho_tabuleiro):
            cabecalho += "   " + letters[i]
            
        return cabecalho

    def tabuleiro_para_str(self):
        linhas = [self.cabecalho()]
        for i in range(tamanho_tabuleiro):
            linha = f"{i+1} " + "-".join(pc.peca_para_str(p) for p in self.tabuleiro_lista[i])
            linhas.append(linha)
            if i < tamanho_tabuleiro - 1:
                if i%2 == 0:
                    linhas.append("   | \\ | / |")
                else:
                    linhas.append("   | / | \\ |")
        return "\n".join(linhas)
        

    @staticmethod
    def tuplo_para_tabuleiro(tp):
        tabuleiro = Tabuleiro()
        for i in range(tamanho_tabuleiro):
            for j in range(tamanho_tabuleiro):
                if tp[i][j] == 1:
                    tabuleiro.tabuleiro_lista[i][j] = pc('X')
                elif tp[i][j] == -1:
                    tabuleiro.tabuleiro_lista[i][j] = pc('O')
                else:
                    tabuleiro.tabuleiro_lista[i][j] = pc(' ')
        return tabuleiro

    # ==============================
    # 5) FUNÇÕES DE ALTO NÍVEL
    # ==============================

    def obter_ganhador(self):
        for i in range(tamanho_tabuleiro):
            if (self.tabuleiro_lista[i][0].player == self.tabuleiro_lista[i][1].player == self.tabuleiro_lista[i][2].player) and self.tabuleiro_lista[i][0].player != ' ':
                return self.tabuleiro_lista[i][0]
        for j in range(tamanho_tabuleiro):
            if (self.tabuleiro_lista[0][j].player == self.tabuleiro_lista[1][j].player == self.tabuleiro_lista[2][j].player) and self.tabuleiro_lista[0][j].player != ' ':
                return self.tabuleiro_lista[0][j]
        return pc(' ')

    def obter_posicoes_livres(self):
        livres = []
        for i in range(tamanho_tabuleiro):
            for j in range(tamanho_tabuleiro):
                if self.tabuleiro_lista[i][j].player == ' ':
                    livres.append(ps(chr(ord('a') + j), str(i + 1)))
        return tuple(livres)

    def obter_posicoes_jogador(self, j):
        posicoes = []
        for i in range(tamanho_tabuleiro):
            for k in range(tamanho_tabuleiro):
                if pc.pecas_iguais(self.tabuleiro_lista[i][k], j):
                    posicoes.append(ps(chr(ord('a') + k), str(i + 1)))
        return tuple(posicoes)

    def posicao_ocupada_por(self, pos, peca):
        """
        Verifica se a posição 'pos' está ocupada pela peça 'peca' indicada.
        Retorna True se sim, False caso contrário.
        """
        return pc.pecas_iguais(self.obter_peca(pos), peca)
