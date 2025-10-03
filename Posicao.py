"""
Módulo: posicao
O TAD posicao é usado para representar uma posição do tabuleiro de jogo. Cada posição é
caraterizada pela coluna e linha que ocupa no tabuleiro. 
"""
"""
Constantes
"""
letters = ('a', 'b', 'c')
nums = (1, 2, 3)

class Posicao:
    
    def __init__(self, c, l):
        self.c = c
        self.l = l

    """
        Construtor que cria a posição partindo de duas cadeias de carateres
        a b c - nas colunas
        1 2 3 - nas linhas
    """
    @staticmethod
    def cria_posicao(c, l):
        if c in letters and l in nums:
            return Posicao(c, l)
        else:
            return ValueError("cria_posicao: argumentos invalidos")
        
    """
    cria_copia_posicao(p) recebe uma posição e devolve uma cópia novada posição.
    """
    @staticmethod
    def cria_copia_posicao(pos):
        return Posicao(pos.c, pos.l)
             
    
    def __repr__(self):
        return f"Posição Criada na coluna '{self.c}' e linha '{self.l}'"