"""
Modulo: peca
O TAD peca e usado para representar as pecas do jogo do moinho.
Cada peca e caracterizada pelo jogador ('X', 'O') ou pode ser livre (' ').
"""


#   Representacao interna: string simples ('X', 'O' ou ' ')


PECAS_VALIDAS = ('X', 'O', ' ')


#   CONSTRUTORES


def cria_peca(identificador_peca):
    """cria_peca: str -> peca
    Cria uma peca correspondente ao jogador indicado ('X', 'O' ou ' ').
    """
    if identificador_peca not in PECAS_VALIDAS:
        raise ValueError("cria_peca: argumento invalido")
    return identificador_peca


def cria_copia_peca(peca):
    """cria_copia_peca: peca -> peca
    Devolve uma copia da peca.
    """
    
    return cria_peca(peca)  



#   RECONHECEDOR

def eh_peca(arg):
    """eh_peca: universal -> booleano
    Devolve True se o argumento representar uma peca valida ('X', 'O' ou ' ').
    """
   
    return arg in PECAS_VALIDAS




#   TESTE


def pecas_iguais(peca1, peca2):
    """pecas_iguais: peca x peca -> booleano
    Devolve True apenas se j1 e j2 sao pecas e sao iguais.
    """
    return eh_peca(peca1) and eh_peca(peca2) and peca1 == peca2



#   TRANSFORMADORES


def peca_para_str(peca):
    """peca_para_str: peca -> str
    Devolve a cadeia '[X]', '[O]' ou '[]' que representa a peca.
    """
    return f"[{peca}]"


#   Funcao de alto nivel


def peca_para_inteiro(peca):
    """peca_para_inteiro: peca -> int
        Devolve:
            1 se a peca e 'X'
         -1 se a peca e 'O'
            0 se a peca e ' ' (livre)
        """
    if pecas_iguais(peca, cria_peca('X')):
        return 1
    elif pecas_iguais(peca, cria_peca('O')):
        return -1
    else:
        return 0



#   FUNCAO AUXILIAR (nao obrigatoria)


def obter_peca_adversario(peca):
    """obter_peca_adversario: peca -> peca
    Devolve a peca do jogador adversario.
    """
    if pecas_iguais(peca, cria_peca('X')):
        return cria_peca('O')
    elif pecas_iguais(peca, cria_peca('O')):
        return cria_peca('X')
    else:
        return cria_peca(' ')
