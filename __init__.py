from Posicao import Posicao as pos


p1 = pos.cria_posicao('a', '2')
p2 = pos.cria_posicao('b', '3')

print(pos.posicoes_iguais(p1, p2))

print(pos.posicao_para_str(p1)) # verificar pelicas se tem que printar com elas
print(isinstance(pos.posicao_para_str(p1), str)) # indicar ser String

print(tuple(pos.posicao_para_str(p) for p in pos.obter_posicoes_adjacentes(p2)))