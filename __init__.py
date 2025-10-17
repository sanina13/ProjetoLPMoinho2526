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
        posicoes = t.obter_posicoes_livres()

        #Vitoria
        """ for pos in posicoes:
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
 """

        
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
        cantos = {ps.cria_posicao(l, c).posicao_para_str() for l in ['a', 'c'] for c in ['1', '3']}
        for pos in posicoes:
            if pos.posicao_para_str() in cantos:
                 return(pos,)



t = tab.cria_tabuleiro()

# Criar peças
x = pc.cria_peca('X')  # computador
o = pc.cria_peca('O')  # adversário


t.coloca_peca(o, ps.cria_posicao('a', '1'))
t.coloca_peca(o, ps.cria_posicao('b', '1'))
t.coloca_peca(o, ps.cria_posicao('c', '1'))
t.coloca_peca(x, ps.cria_posicao('b', '2'))   

movimento = obter_movimento_auto(t, x, 'facil')
print("Movimento escolhido:", movimento)
        
     
            

        
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




        