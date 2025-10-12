"""
Módulo: posicao
O TAD posicao é usado para representar uma posição do tabuleiro de jogo. Cada posição é
caraterizada pela coluna e linha que ocupa no tabuleiro. 
"""
"""
Constantes
"""
letters = ('a', 'b', 'c')
nums = ('1', '2', '3')

class Posicao:
    
    def __init__(self, c, l):
        if not c in letters and l in nums:
            raise ValueError("cria_posicao: argumentos invalidos")
        self.c = c
        self.l = l

    """
        Construtor que cria a posição partindo de duas cadeias de carateres
        a b c - nas colunas
        1 2 3 - nas linhas
    """
    @staticmethod
    def cria_posicao(c, l):
        return Posicao(c, l)
        
        
    """
    cria_copia_posicao(p) recebe uma posição e devolve uma cópia nova da posição.
    """
    @staticmethod
    def cria_copia_posicao(pos):
        return Posicao(pos.c, pos.l)
    

    """
        Seletores obter_pos_c e obter_pos_l
    """

    def obter_pos_c(self):
        return self.c

    def obter_pos_l(self):
        return self.l  
    
    """
        Reconhecedor: o eh_posicao: universal → booleano eh_posicao(arg) 
        devolve True caso o seu argumento seja um TAD posicao e False caso contrário.
    """
    def eh_posicao(arg):
        """if isinstance(arg, Posicao):"""
        return isinstance(arg, Posicao) and arg.c in letters and arg.l in nums
        """ Codigo que so seria necessario se nao se colocar uma POS 
            elif isinstance(arg, tuple):
            if len(arg) != 2:
                return False
            try: 
                return arg[0] in letters and int(arg[1]) in nums
            except ValueError:
                return False"""
        
    """
        Teste: o posicoes_iguais: posicao × posicao → booleano
        posicoes_iguais(p1,p2) devolve True apenas se p1 e p2 são posições esão iguais.
    """
    def posicoes_iguais(self, other):
        return self.c == other.c and self.l == other.l
    
    """
        Transformador: o posição_para_str: posicao → str
        posicao_para_str(p) devolve a cadeia de caracteres ‘cl’ que representa
        o seu argumento, sendo os valores c e l as componentes coluna e linha de p. 
    """
    def posicao_para_str(self):
        return f"{self.c}{self.l}"
    
    """
       Função de alto nível:
        o obter_posicoes_adjacentes: posicao → tuplo de posicoes
        obter_posicoes_adjacentes(p) devolve um tuplo com as posições
        adjacentes à posição p de acordo com a ordem de leitura do tabuleiro. 
    """

    def obter_posicoes_adjacentes(self):
        # Converter coluna para número temporário (para facilitar cálculos)
        # 'a' -> 1, 'b' -> 2, 'c' -> 3
        # Utilizei o chat para essa conversão porque com um switch o codigo
        # ficava poluido e assim com ASCII ele converte de letra para numero
        col_num = ord(self.c) - ord('a') + 1
        linha_num = int(self.l)
        
        # Esses são os deslocamentos que eu pelo menos entendi tendo em conta que seriam apenas os adjacentes
        deslocamentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pos_adjacentes = []

        for dl, dc in deslocamentos:
            linha_nova = linha_num + dl
            col_nova = col_num + dc

            if 1 <= linha_nova <= 3 and 1<= col_nova <=3:
                col_letra = chr(ord('a') + col_nova - 1)
                pos_adjacentes.append(Posicao(col_letra, str(linha_nova)))


        return tuple(pos_adjacentes)
        
        

    def __repr__(self):
        return f"Posição Criada na coluna '{self.c}' e linha '{self.l}'"
    
