from logic.movimentos import * 
from logic.moinho import *
# imports para simular a stream de input/output
import io
import sys

num_tests = 0
total_score = 0

print("Inicio dos testes publicos")
print("---------------------")

# TAD posicao
num_tests += 1
try:
    posicao1 = cria_posicao('a', '4')
    print("Teste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "cria_posicao: argumentos invalidos":
        total_score += 1
        print("Teste " + str(num_tests) + ": Passou")
    else:
        print("Teste " + str(num_tests) + ": Falhou")
except:
    print("Teste " + str(num_tests) + ": Falhou")
    pass

num_tests += 1
posicao1 = cria_posicao('a', '2')
posicao2 = cria_posicao('b', '3')
if not posicoes_iguais(posicao1, posicao2):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
posicao1 = cria_posicao('a', '2')
if posicao_para_str(posicao1) == "a2":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
posicao2 = cria_posicao('b', '3')
tuplo_adjacentes = tuple(posicao_para_str(posicao) for posicao in obter_posicoes_adjacentes(posicao2))

if tuplo_adjacentes == ('b2', 'a3', 'c3'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# TAD peca
num_tests += 1
try:
    peca1 = cria_peca('x')
    print("Teste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "cria_peca: argumento invalido":
        total_score += 1
        print("Teste " + str(num_tests) + ": Passou")
    else:
        print("Teste " + str(num_tests) + ": Falhou")
except:
    print("Teste " + str(num_tests) + ": Falhou")
    pass

num_tests += 1
peca1 = cria_peca('X')
peca2 = cria_peca('O')
if not pecas_iguais(peca1, peca2):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
peca1 = cria_peca('X')
if peca_para_str(peca1) == "[X]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
if peca_para_inteiro(cria_peca(' ')) == 0:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

 # TAD tabuleiro
num_tests += 1
tabuleiro = cria_tabuleiro()
str_tabuleiro = tabuleiro_para_str(coloca_peca(tabuleiro, cria_peca('X'), cria_posicao('a', '1')))
if str_tabuleiro == "   a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[ ]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = cria_tabuleiro()
tabuleiro_resultado = coloca_peca(tabuleiro, cria_peca('X'), cria_posicao('a', '1'))
str_tabuleiro = tabuleiro_para_str(coloca_peca(tabuleiro, cria_peca('O'), cria_posicao('b', '2')))
if str_tabuleiro == "   a   b   c\n1 [X]-[ ]-[ ]\n   | \ | / |\n2 [ ]-[O]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = cria_tabuleiro()
tabuleiro_resultado = coloca_peca(tabuleiro, cria_peca('X'), cria_posicao('a', '1'))
tabuleiro_resultado = coloca_peca(tabuleiro, cria_peca('O'), cria_posicao('b', '2'))
str_tabuleiro = tabuleiro_para_str(move_peca(tabuleiro, cria_posicao('a', '1'), cria_posicao('b', '1')))
if str_tabuleiro == "   a   b   c\n1 [ ]-[X]-[ ]\n   | \ | / |\n2 [ ]-[O]-[ ]\n   | / | \ |\n3 [ ]-[ ]-[ ]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
str_tabuleiro = tabuleiro_para_str(tabuleiro)
if str_tabuleiro == "   a   b   c\n1 [ ]-[X]-[O]\n   | \ | / |\n2 [ ]-[X]-[O]\n   | / | \ |\n3 [X]-[ ]-[O]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
str_peca_ganhadora = peca_para_str(obter_ganhador(tabuleiro))
if str_peca_ganhadora == "[O]":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo_posicoes_livres = tuple(posicao_para_str(posicao) for posicao in obter_posicoes_livres(tabuleiro))
if tuplo_posicoes_livres == ('a1', 'a2', 'b3'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo_pecas_coluna_a = tuple(peca_para_str(peca) for peca in obter_vetor(tabuleiro, 'a'))
if tuplo_pecas_coluna_a == ('[ ]', '[ ]', '[X]'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (-0, 1, -1), (1, 0, -1)))
tuplo_pecas_linha_2 = tuple(peca_para_str(peca) for peca in obter_vetor(tabuleiro, '2'))
if tuplo_pecas_linha_2 == ('[ ]', '[X]', '[O]'):
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

# obter_movimento_manual
def obter_movimento_manual_teste(tabuleiro_teste, peca_teste, entrada_jogada):
    sys.stdin = io.StringIO(entrada_jogada)
    movimento = obter_movimento_manual(tabuleiro_teste, peca_teste)
    for line in sys.stdin:
        print(line)
    return movimento


num_tests += 1
try:
    tabuleiro = cria_tabuleiro()
    movimento = obter_movimento_manual_teste(tabuleiro, cria_peca('X'), 'a1')
    if posicao_para_str(movimento[0]) == "a1":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

num_tests += 1
try:
    tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (1, -1, 0), (1, -1, 0)))
    movimento = obter_movimento_manual_teste(tabuleiro, cria_peca('X'), 'b1a1')
    if posicao_para_str(movimento[0]) == "b1" and posicao_para_str(movimento[1]) == "a1" and len(movimento) == 2:
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

num_tests += 1
try:
    tabuleiro = tuplo_para_tabuleiro(((0, 1, -1), (1, -1, 0), (1, -1, 0)))
    movimento = obter_movimento_manual_teste(tabuleiro, cria_peca('O'), 'a2a1')
    print("\nTeste " + str(num_tests) + ": Falhou")
except ValueError as inst:
    if str(inst) == "obter_movimento_manual: escolha invalida":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass

# obter_movimento_auto
num_tests += 1
tabuleiro = cria_tabuleiro()
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil')
if posicao_para_str(movimento[0]) == "b2":
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((1, 0, -1), (0, 1, -1), (1, -1, 0)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'facil')
if posicao_para_str(movimento[0]) == "a1" and posicao_para_str(movimento[1]) == "b1" and len(movimento) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((1, 0, -1), (0, 1, -1), (1, -1, 0)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal')
if posicao_para_str(movimento[0]) == "b2" and posicao_para_str(movimento[1]) == "a2" and len(movimento) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((1, -1, -1), (-1, 1, 0), (0, 0, 1)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'normal')
if posicao_para_str(movimento[0]) == "b2" and posicao_para_str(movimento[1]) == "c2" and len(movimento) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")

num_tests += 1
tabuleiro = tuplo_para_tabuleiro(((1, -1, -1), (-1, 1, 0), (0, 0, 1)))
movimento = obter_movimento_auto(tabuleiro, cria_peca('X'), 'dificil')
if posicao_para_str(movimento[0]) == "c3" and posicao_para_str(movimento[1]) == "c2" and len(movimento) == 2:
    total_score += 1
    print("Teste " + str(num_tests) + ": Passou")
else:
    print("Teste " + str(num_tests) + ": Falhou")


# moinho


def moinho_teste(jogador, modo, jogadas):
    sys.stdin = io.StringIO(jogadas)
    fim = moinho(jogador, modo)
    for line in sys.stdin:
        print(line)
    return fim


num_tests += 1
try:
    fim = moinho_teste('[X]', 'facil', 'a2\na1\nc1\nc1c2\na1b1\nb1b2')
    if fim == "[X]":
        total_score += 1
        print("\nTeste " + str(num_tests) + ": Passou")
    else:
        print("\nTeste " + str(num_tests) + ": Falhou")
except:
    print("\nTeste " + str(num_tests) + ": Falhou")
    pass 

print("---------------------")
print("Pontuacao final do projeto: ", total_score, "/", num_tests, "(" + "{:.2f}".format((total_score / num_tests) * 100) + "% )")
