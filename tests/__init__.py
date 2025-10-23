#testes nivel automatico
""" t = tab.cria_tabuleiro() 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'facil') 
print(ps.posicao_para_str(m[0]))

t = tab.tuplo_para_tabuleiro(((1,0,-1),(0,1,-1),(1,-1,0))) 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'facil') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

m = obter_movimento_auto(t, pc.cria_peca('X'), 'normal') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

t = tab.tuplo_para_tabuleiro(((1,-1,-1),(-1,1,0),(0,0,1))) 
m = obter_movimento_auto(t, pc.cria_peca('X'), 'normal') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))

m = obter_movimento_auto(t, pc.cria_peca('X'), 'dificil') 
print(ps.posicao_para_str(m[0]), ps.posicao_para_str(m[1]))
 """

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
"""
""" for linha in tabuleiro.tabuleiro_lista:
    for peca in linha:
        print("["+ pc.peca_para_str(peca) +"]", end='')
    print()  """
"""
print (tabuleiro.tabuleiro_para_str())
tabuleiro.coloca_peca(j1, p1)
vet = tabuleiro.obter_vetor('2')
print([pc.peca_para_str(p) for p in vet]) """




        