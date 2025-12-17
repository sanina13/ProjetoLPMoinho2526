"""
Modulo: posicao
O TAD posicao e usado para representar uma posicao do tabuleiro de jogo. Cada posicao
e caracterizada pela coluna e linha que ocupa no tabuleiro.
"""

# Constantes
LETRAS = ('a', 'b', 'c')
NUMS = ('1', '2', '3')



#   CONSTRUTORES

def cria_posicao(coluna, linha):
    """cria_posicao: str x str -> posicao
    Cria uma posicao (tuplo) a partir da coluna c e linha l.
    """
    if coluna not in LETRAS or linha not in NUMS:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (coluna, linha)


def cria_copia_posicao(posicao):
    """cria_copia_posicao: posicao -> posicao"""
    return cria_posicao(obter_pos_c(posicao), obter_pos_l(posicao))



#   SELETORES

def obter_pos_c(posicao):
    """obter_pos_c: posicao -> str"""
    return posicao[0]


def obter_pos_l(posicao):
    """obter_pos_l: posicao -> str"""
    return posicao[1]


#   RECONHECEDOR

def eh_posicao(argumento):
    """eh_posicao: universal -> booleano"""
    try:
        coluna, linha = argumento[0], argumento[1]
        return len(argumento) == 2 and coluna in LETRAS and linha in NUMS
    except Exception:
        return False


#   TESTE

def posicoes_iguais(posicao1, posicao2):
    """posicoes_iguais: posicao x posicao -> booleano"""
    return eh_posicao(posicao1) and eh_posicao(posicao2) and posicao1 == posicao2


#   TRANSFORMADOR

def posicao_para_str(posicao):
    """posicao_para_str: posicao -> str"""
    return posicao[0] + posicao[1]


#   FUNCAO DE ALTO NIVEL

def obter_posicoes_adjacentes(posicao):
    """obter_posicoes_adjacentes: posicao -> tuplo de posicoes"""
    coluna= obter_pos_c(posicao)
    linha = obter_pos_l(posicao)
    
    adjacentes = []

    numero_coluna = ord(coluna) - ord('a') + 1
    numero_linha = int(linha)

    # ordem: cima, esquerda, direita, baixo
    deslocamentos = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    
    if numero_coluna == numero_linha or (numero_coluna + numero_linha) == 4:
        deslocamentos.extend([(-1, -1), (1, 1), (-1, 1), (1, -1)])

    for delta_coluna, delta_linha in deslocamentos:
        nova_coluna_num = numero_coluna + delta_coluna
        nova_linha_num = numero_linha + delta_linha
        if 1 <= nova_coluna_num <= 3 and 1 <= nova_linha_num <= 3:
            adjacentes.append(
                cria_posicao(chr(ord('a') + nova_coluna_num - 1), str(nova_linha_num))
            )
    
    adjacentes.sort(key=lambda p: (int(obter_pos_l(p)), obter_pos_c(p)))       

    return tuple(adjacentes)
