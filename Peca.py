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
        

    @staticmethod
    def cria_peca(player):
        return Peca(player)

    @staticmethod
    def cria_copia_peca(piece):
        """
        Cria uma cópia da peça fornecida.
        """
        return Peca(piece.player)


    '''
     @staticmethod 
        def eh_peca(arg): 
            "" Verifica se o argumento é uma peça válida. """ 
        return arg.piece in possible_piece_type
    '''
    
    def eh_peca(arg):
        return type(arg) == Peca and arg.player in possible_piece_type

    #colocação do self para comparar algo com outra peca
    def __eq__(self, other):
        return self.pecas_iguais(self, other)
        
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
