import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.movimentos import *

#testes nivel automatico
tabuleiro = cria_tabuleiro() 
m = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil') 
print(posicao_para_str(m[0]))

tabuleiro = tuplo_para_tabuleiro(((1,0,-1),(0,1,-1),(1,-1,0))) 
m = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil') 
print(posicao_para_str(m[0]), posicao_para_str(m[1]))

m = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal') 
print(posicao_para_str(m[0]), posicao_para_str(m[1]))

tabuleiro = tuplo_para_tabuleiro(((1,-1,-1),(-1,1,0),(0,0,1))) 
m = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal') 
print(posicao_para_str(m[0]), posicao_para_str(m[1]))

m = obter_movimento_auto(tabuleiro, cria_peca('X'), 'dificil') 
print(posicao_para_str(m[0]), posicao_para_str(m[1]))


#testes anteriores
p1 = cria_posicao('a', '2')
p2 = cria_posicao('a', '2')

print(posicoes_iguais(p1, p2))

print(posicao_para_str(p1)) # verificar pelicas se tem que printar com elas
print(isinstance(posicao_para_str(p1), str)) # indicar ser String

print(tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(p2)))

j1 = cria_peca('X')
j2 = cria_peca('X')

print(pecas_iguais(j1, j2))
print(peca_para_str(j1))
print(peca_para_inteiro(cria_peca(' ')))

tabuleiro = cria_tabuleiro()

for linha in tabuleiro:
    for peca in linha:
        print("["+ peca_para_str(peca) +"]", end='')
    print()  

print (tabuleiro_para_str(tabuleiro))
coloca_peca(tabuleiro, j1, p1)
vet = obter_vetor(tabuleiro, '2')
print([peca_para_str(p) for p in vet]) 


        