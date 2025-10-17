from Posicao import Posicao as ps
from Peca import Peca as pc
from Tabuleiro import Tabuleiro as tab



""" t = tab.cria_tabuleiro()

# Criar peça do jogador 'X'
x = pc.cria_peca('X')
# Criar peça do adversário 'O'
o = pc.cria_peca('O')
 """
def obter_movimento_auto(t, peca, nivel):
    if len(t.obter_posicoes_jogador(peca)) < 3:
       movimento_colocao(t, peca)
    else:
        movimento_movimentacao(t, peca, nivel)


#função auxiliar para fase de movimento colocação
def movimento_colocao(t, peca):
    posicoes = t.obter_posicoes_livres()

    #Vitoria
    for pos in posicoes:
        t_sim = tab.cria_copia_tabuleiro(t)
        t_sim.coloca_peca(peca, pos)
            
        if t_sim.obter_ganhador().peca_para_inteiro() == peca.peca_para_inteiro():
            return(pos,) 
        
    #Bloqueio
    #se 'X', o adversário é 'O', e vice-versa.
    adversario = pc.cria_peca('O' if peca.player == 'X' else 'X')
        
    for pos in posicoes:
        t_sim = tab.cria_copia_tabuleiro(t)
        t_sim.coloca_peca(adversario, pos)
            
        if t_sim.obter_ganhador().peca_para_inteiro() == adversario.peca_para_inteiro(): 
            return(pos,)

    #Centro
    centro = ps.cria_posicao('b', '2')
    if t.eh_posicao_livre(centro):
        return(centro, )
       
    #canto vazio
    """ cantos = [ps.cria_posicao('a', '1').posicao_para_str(), 
                  ps.cria_posicao('a', '3').posicao_para_str(), 
                  ps.cria_posicao('c', '1').posicao_para_str(), 
                  ps.cria_posicao('c', '3').posicao_para_str()] """
    #Versão otimizada com ajuda da ia
    cantos = {ps.cria_posicao(l, c) for l in ['a', 'c'] for c in ['1', '3']}
    for pos in posicoes:
        for canto in cantos:
            if canto.posicoes_iguais(pos):
                return(pos,) 
        
    #Laterais Vazias a2, b1, b3, c2
    """ laterais = [ps.cria_posicao('a', '2').posicao_para_str(), 
                  ps.cria_posicao('b', '1').posicao_para_str(), 
                  ps.cria_posicao('b', '3').posicao_para_str(), 
                  ps.cria_posicao('c', '2').posicao_para_str()]  """
    laterais = {ps.cria_posicao(l,c) for l, c in [('a', '2'), ('b', '1'), ('b', '3'), ('c', '2')]}
    for pos in posicoes:
        for lateral in laterais:
            if lateral.posicoes_iguais(pos):
                return(pos,)

def movimento_movimentacao(t, peca, nivel):
    # testar se existem peças bloqueadas
    posicoes_jogador = t.obter_posicoes_jogador(peca)
    
    movimentos_possiveis = []

    for origem in posicoes_jogador:
        adjacentes = ps.obter_posicoes_adjacentes(origem)
        for destino in adjacentes:
            if t.eh_posicao_livre(destino):
                movimentos_possiveis.append((origem, destino))

    #Se não houver movimentos possiveis retorna a primeira posicao do jogador
    if not movimentos_possiveis:
        primeira = posicoes_jogador[0]
        return (primeira, primeira)
    
    # Níveis

    '''facil a peça a movimentar é sempre a que ocupa a primeira posição em
    ordem de leitura do tabuleiro que tenha alguma posição adjacente livre. A posição de
    destino é a primeira posição adjacente livre.'''

    if nivel == 'facil':
        return movimentos_possiveis[0]

    #normal a incluir o algoritmo minimax


    #dificil a incluir o algoritmo minimax


# Por fazer para nivel normal e dificil
def minimax(n):
    return n

t = tab.cria_tabuleiro()
x = pc.cria_peca('X')

# criar um tabuleiro com algumas peças
t.coloca_peca(x, ps.cria_posicao('b', '2'))
t.coloca_peca(pc.cria_peca('O'), ps.cria_posicao('a', '1'))
t.coloca_peca(pc.cria_peca('O'), ps.cria_posicao('c', '1'))
t.coloca_peca(pc.cria_peca('O'), ps.cria_posicao('b', '1'))

mov = movimento_movimentacao(t, x, 'facil')
print("Movimento escolhido:", ps.posicao_para_str(mov[0]), "→", ps.posicao_para_str(mov[1]))

        
     
            

        
#Testes para a def movimento auto
""" t.coloca_peca(x, pos.cria_posicao('a', '1'))
t.coloca_peca(x, pos.cria_posicao('b', '1'))
t.coloca_peca(o, pos.cria_posicao('a', '2'))
movimento = obter_movimento_auto(t, x, 'facil')
print("Movimento escolhido:", movimento)

t = tab.cria_tabuleiro()

# Peças
x = pc.cria_peca('X')  # computador
o = pc.cria_peca('O')  # adversário

t.coloca_peca(o, pos.cria_posicao('a', '1'))
t.coloca_peca(o, pos.cria_posicao('b', '1'))
t.coloca_peca(x, pos.cria_posicao('a', '2'))
movimento = obter_movimento_auto(t, x, 'facil')
print("Movimento escolhido pelo computador:", movimento) """



#testes anteriores


""" p1 = pos.cria_posicao('a', '2')
p2 = pos.cria_posicao('a', '3')

print(p1.posicoes_iguais(p2))

print(pos.posicao_para_str(p1)) # verificar pelicas se tem que printar com elas
print(isinstance(pos.posicao_para_str(p1), str)) # indicar ser String

print(tuple(pos.posicao_para_str(p) for p in pos.obter_posicoes_adjacentes(p2)))

j1 = pc.cria_peca('X')
j2 = pc.cria_peca('X')

print(j1.pecas_iguais(j2))
print(pc.peca_para_str(j1))
print(pc.peca_para_inteiro(pc.cria_peca(' ')))

tabuleiro = tab.cria_tabuleiro()

for linha in tabuleiro.tabuleiro_lista:
    for peca in linha:
        print("["+ pc.peca_para_str(peca) +"]", end='')
    print() 

tabuleiro.coloca_peca(j1, p1)
vet = tabuleiro.obter_vetor('2')
print([pc.peca_para_str(p) for p in vet]) """




        