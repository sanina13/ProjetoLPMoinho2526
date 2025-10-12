from Posicao import Posicao as pos
from peca import peca as pc


p1 = pos.cria_posicao('a', '2')
p2 = pos.cria_posicao('a', '2')

print(pos.posicoes_iguais(p1, p2))

print(pos.posicao_para_str(p1)) # verificar pelicas se tem que printar com elas
print(isinstance(pos.posicao_para_str(p1), str)) # indicar ser String

print(tuple(pos.posicao_para_str(p) for p in pos.obter_posicoes_adjacentes(p2)))

j1 = pc.cria_peca('X')
j2 = pc.cria_peca('X')

print(pc.pecas_iguais(j1, j2))
print(pc.peca_para_str(j1))
print(pc.peca_para_inteiro(pc.cria_peca(' ')))