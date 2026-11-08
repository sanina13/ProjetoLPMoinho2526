import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.Movimentos import *

# testes nivel automatico
tabuleiro = cria_tabuleiro()
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil')
print(posicao_para_str(movimento[0]))

tabuleiro = tuplo_para_tabuleiro(((1,0,-1),(0,1,-1),(1,-1,0)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil')
print(posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))

movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal')
print(posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))

tabuleiro = tuplo_para_tabuleiro(((1,-1,-1),(-1,1,0),(0,0,1)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal')
print(posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))

movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'dificil')
print(posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))


# testes anteriores
posicao1 = cria_posicao('a', '2')
posicao2 = cria_posicao('a', '2')

print(posicoes_iguais(posicao1, posicao2))

print(posicao_para_str(posicao1))  # verificar pelicas se tem que printar com elas
print(isinstance(posicao_para_str(posicao1), str))  # indicar ser String

print(tuple(posicao_para_str(p) for p in obter_posicoes_adjacentes(posicao2)))

peca1 = cria_peca('X')
peca2 = cria_peca('X')

print(pecas_iguais(peca1, peca2))
print(peca_para_str(peca1))
print(peca_para_inteiro(cria_peca(' ')))

tabuleiro = cria_tabuleiro()

for linha in tabuleiro:
    for peca in linha:
        print("[" + peca_para_str(peca) + "]", end='')
    print()

print(tabuleiro_para_str(tabuleiro))
coloca_peca(tabuleiro, peca1, posicao1)
vetor_pecas = obter_vetor(tabuleiro, '2')
print([peca_para_str(p) for p in vetor_pecas])
