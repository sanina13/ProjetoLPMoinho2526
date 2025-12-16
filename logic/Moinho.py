# moinho.py
from logic.Movimentos import *

def moinho(jogador_inicial, modo):
    # validar argumentos
    if jogador_inicial not in ('[X]', '[O]') or modo not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')

    tabuleiro = cria_tabuleiro()
    pecah = cria_peca(jogador_inicial[1])          # humano
    pecac = obter_peca_adversario(pecah)           # computador
    peca_atual = cria_peca('X')                    # começa o X

    print(f"Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {modo}.")

    while True:
        print(tabuleiro_para_str(tabuleiro))

        # decidir se é turno do humano (manual) ou do computador (auto)
        if pecas_iguais(peca_atual, pecah):
            movimento = obter_movimento(tabuleiro, peca_atual)           # manual
        else:
            print(f"Turno do computador ({modo}):")
            movimento = obter_movimento(tabuleiro, peca_atual, modo)     # automático

        # aplicar movimento
        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            print(tabuleiro_para_str(tabuleiro))
            return peca_para_str(ganhador)

        peca_atual = obter_peca_adversario(peca_atual)