# moinho.py
from logic.Movimentos import *

def moinho(jogador_inicial, modo):
    tabuleiro = cria_tabuleiro()
    peca_atual = cria_peca(jogador_inicial[1])

    while True:
        print(tabuleiro_para_str(tabuleiro))
        try:
            if modo is None:
                movimento = obter_movimento(tabuleiro, peca_atual)
            else:
                movimento = obter_movimento(tabuleiro, peca_atual, modo)
        except ValueError:
            continue

        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            print(tabuleiro_para_str(tabuleiro))
            return peca_para_str(ganhador)
        peca_atual = obter_peca_adversario(peca_atual)