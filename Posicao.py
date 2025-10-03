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
    

    """
        Seletores obter_pos_c e obter_pos_l
    """

    def obter_pos_c(p):
        return p.c

    def obter_pos_l(p):
        return p.l  
    
    """
        Reconhecedor: o eh_posicao: universal → booleano eh_posicao(arg) 
        devolve True caso o seu argumento seja um TAD posicao e False caso contrário.
    """
    def eh_posicao(arg):
        if isinstance(arg, Posicao):
            return arg.c in letters and arg.l in nums
        elif isinstance(arg, tuple):
            if len(arg) != 2:
                return False
            try: 
                return arg[0] in letters and int(arg[1]) in nums
            except ValueError:
                return False
        return False
    
    """
        Teste: o posicoes_iguais: posicao × posicao → booleano
        posicoes_iguais(p1,p2) devolve True apenas se p1 e p2 são posições esão iguais.
    """

    
             
    
    def __repr__(self):
        return f"Posição Criada na coluna '{self.c}' e linha '{self.l}'"