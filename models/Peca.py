"""
Módulo: peca
O TAD peca é usado para representar as peças do jogo do moinho.
Cada peça é caracterizada pelo jogador ('X', 'O') ou pode ser livre ('').
"""

# ============================================================
#   Representação interna: string simples ('X', 'O' ou ' ')
# ============================================================

PECAS_VALIDAS = ('X', 'O', '')

# ================================
#   CONSTRUTORES
# ================================

def cria_peca(identificador_peca):
    """cria_peca: str → peca
    Cria uma peça correspondente ao jogador indicado ('X', 'O' ou '').
    """
    if identificador_peca not in PECAS_VALIDAS:
        raise ValueError("cria_peca: argumento invalido")
    return identificador_peca


def cria_copia_peca(peca):
    """cria_copia_peca: peca → peca
    Devolve uma cópia da peça.
    """
    
    return cria_peca(peca)  


# ================================
#   RECONHECEDOR
# ================================

def eh_peca(arg):
    """eh_peca: universal → booleano
    Devolve True se o argumento representar uma peça válida ('X', 'O' ou '').
    """
   
    return arg in PECAS_VALIDAS



# ================================
#   TESTE
# ================================

def pecas_iguais(peca1, peca2):
    """pecas_iguais: peca × peca → booleano
    Devolve True apenas se j1 e j2 são peças e são iguais.
    """
    return eh_peca(peca1) and eh_peca(peca2) and peca1 == peca2


# ================================
#   TRANSFORMADORES
# ================================

def peca_para_str(peca):
    """peca_para_str: peca → str
    Devolve a cadeia '[X]', '[O]' ou '[]' que representa a peça.
    """
    return f"[{peca}]"

# ================================
#   Função de alto nivel
# ================================

def peca_para_inteiro(peca):
    """peca_para_inteiro: peca → int
    Devolve:
      1 se a peça é 'X'
     -1 se a peça é 'O'
      0 se a peça é '' (livre)
    """
    if pecas_iguais(peca, cria_peca('X')):
        return 1
    elif pecas_iguais(peca, cria_peca('O')):
        return -1
    else:
        return 0


# ================================
#   FUNÇÃO AUXILIAR (não obrigatória)
# ================================

def obter_peca_adversario(peca):
    """obter_peca_adversario: peca → peca
    Devolve a peça do jogador adversário.
    """
    if pecas_iguais(peca, cria_peca('X')):
        return cria_peca('O')
    elif pecas_iguais(peca, cria_peca('O')):
        return cria_peca('X')
    else:
        return cria_peca('')
