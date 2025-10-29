"""
O TAD peca é usado para representar as peças do jogo. Cada peça é caracterizada
pelo jogador a quem pertence, podendo ser peças do jogador 'X' ou do jogador 'O'.
Por conveniência, é também definido o conceito de peça livre (' ').
"""

possible_piece_type = ('O', ' ', 'X')  # tuplo com as opções válidas de peças

class Peca:
    """
    Classe que representa uma peça do jogo do moinho.
    Cada peça pertence a um jogador ('X' ou 'O') ou pode ser livre (' ').
    """

    def __init__(self, player):
        """
        Cria uma nova peça para o jogador indicado.
        Retorna uma instância de peca se o jogador for válido.
        Lança ValueError se o argumento for inválido.
        """
        if not player in possible_piece_type:
            raise ValueError("cria_peca: argumento invalido")
        """
        Iniciali4za uma peça com o jogador especificado.
        player: 'X', 'O' ou ' ' (livre)
        """
        self.player = player
        

    @classmethod
    def cria_peca(cls, player):
        """Fábrica: devolve uma instância da classe (suporta subclasses)."""
        return cls(player)

    @classmethod
    def cria_copia_peca(cls, piece):
        """
        Cria uma cópia da peça fornecida (devolve instância de cls).
        """
        return cls(piece.player)


    '''
     @staticmethod 
        def eh_peca(arg): 
            "" Verifica se o argumento é uma peça válida. """ 
        return arg.piece in possible_piece_type
    '''
    @classmethod
    def eh_peca(cls, arg):
        """Reconhecedor: aceita instâncias da classe (suporta herança)."""
        return isinstance(arg, cls) and arg.player in possible_piece_type
        # Se preferires não aceitar subclasses, usar: return type(arg) == cls and arg.player in possible_piece_type

    @classmethod
    def obter_Peca_adversario(cls, peca):
        """Cria uma peça do jogador adversário."""
        return cls.cria_peca('O' if peca.obter_jogador() == 'X' else 'X')
    
    
    def obter_jogador(self):
        return self.player
    
    def obter_adversario(self):
        return 'O' if self.obter_jogador() == 'X' else 'X'
    
    #colocação do self para comparar algo com outra peca
    def __eq__(self, other):
        """Permite comparar duas peças com ==."""
        if not isinstance(other, Peca):
            return False
        return self.player == other.player

    def pecas_iguais(self, other): 
        """
        Verifica se duas peças pertencem ao mesmo jogador.
        """
        return self.player == other.player

    
    def peca_para_str(self):
        """
        Devolve a representação em string da peça (o símbolo do jogador).
        """
        return "[" + self.player + "]"

    
    def peca_para_inteiro(self):
        """
        Converte a peça para um valor inteiro:
        -1 para 'O', 0 para ' ' (livre), 1 para 'X'.
        """
        return possible_piece_type.index(self.player) - 1

    def __repr__(self):
        return f"Peca('{self.player}')"