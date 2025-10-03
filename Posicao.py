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
    """
        Construtor que cria a posição partindo de duas cadeias de carateres
        a b c - nas colunas
        1 2 3 - nas linhas
    """
    def __init__(self, c, l):
        self.c = c
        self.l = l


    @staticmethod
    def cria_posicao(c, l):
        if c in letters and l in nums:
            return Posicao(c, l)
        else:
            return ValueError("cria_posicao: argumentos invalidos")
             
    
    def __repr__(self):
        return "Posição Criada"