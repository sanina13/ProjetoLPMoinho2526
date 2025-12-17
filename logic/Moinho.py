# moinho.py
from logic.Movimentos import *

def moinho(jogador_inicial, modo):
    """
    moinho: str x str -> str
    Permite jogar um jogo completo do Jogo do Moinho contra o computador.
    """

    # validar argumentos
    if jogador_inicial not in ('[X]', '[O]') or modo not in ('facil', 'normal', 'dificil'):
        raise ValueError("moinho: argumentos invalidos")

    tabuleiro = cria_tabuleiro()

    peca_humano = cria_peca(jogador_inicial[1])
    peca_computador = obter_peca_adversario(peca_humano)

    # X joga sempre primeiro
    peca_atual = cria_peca('X')

    print(f"Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {modo}.")

    # imprimir tabuleiro inicial
    print(tabuleiro_para_str(tabuleiro))

    while True:

        # turno do humano
        if pecas_iguais(peca_atual, peca_humano):
            movimento = obter_movimento(tabuleiro, peca_atual)

        # turno do computador
        else:
            print(f"Turno do computador ({modo}):")
            movimento = obter_movimento(tabuleiro, peca_atual, modo)

        # aplicar movimento
        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        # imprimir tabuleiro apos jogada
        print(tabuleiro_para_str(tabuleiro))

        # verificar ganhador
        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            return peca_para_str(ganhador)

        # trocar jogador
        peca_atual = obter_peca_adversario(peca_atual)
