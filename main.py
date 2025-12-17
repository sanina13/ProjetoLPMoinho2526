# main.py
from logic.Moinho import *
from models.Tabuleiro import *


def jogo_humano_vs_computador():
    # escolher peca do humano
    while True:
        escolha = input("Escolha o jogador humano (X/O): ").strip().upper()
        if escolha in ('X', 'O'):
            jogador_humano = f'[{escolha}]'
            break
        print("Escolha invalida. Introduza 'X' ou 'O'.")

    # escolher dificuldade
    niveis = {'1': 'facil', '2': 'normal', '3': 'dificil'}
    while True:
        escolha_n = input("Escolha a dificuldade do computador: 1-facil 2-normal 3-dificil: ").strip()
        if escolha_n in niveis:
            nivel = niveis[escolha_n]
            break
        print("Escolha invalida. Tente novamente.")

    tabuleiro = cria_tabuleiro()
    pecah = cria_peca(jogador_humano[1])
    pecac = obter_peca_adversario(pecah)
    peca_atual = cria_peca('X')

    print(f"Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {nivel}.")
    print(tabuleiro_para_str(tabuleiro))

    while True:
        try:
            # turno do humano
            if pecas_iguais(peca_atual, pecah):
                movimento = obter_movimento(tabuleiro, peca_atual)
            # turno do computador
            else:
                print(f"Turno do computador ({nivel}):")
                movimento = obter_movimento(tabuleiro, peca_atual, nivel)

        except ValueError as e:
            if str(e) == "obter_movimento_manual: escolha invalida":
                print("Jogada invalida. Tente novamente.")
                continue
            else:
                raise

        # aplicar movimento
        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        print(tabuleiro_para_str(tabuleiro))

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            print("Vencedor:", peca_para_str(ganhador))
            return

        peca_atual = obter_peca_adversario(peca_atual)


def jogo_humano_vs_humano():
    tabuleiro = cria_tabuleiro()
    peca_atual = cria_peca('X')

    print(tabuleiro_para_str(tabuleiro))

    while True:
        try:
            movimento = obter_movimento(tabuleiro, peca_atual)
        except ValueError as e:
            if str(e) == "obter_movimento_manual: escolha invalida":
                print("Jogada invalida. Tente novamente.")
                continue
            else:
                raise

        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        print(tabuleiro_para_str(tabuleiro))

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            print("Vencedor:", peca_para_str(ganhador))
            return

        peca_atual = obter_peca_adversario(peca_atual)


def main():
    menu = (
        "\nMini Menu - Escolha o modo de jogo:\n"
        "1 - Jogador (X/O) vs Computador\n"
        "2 - Jogador vs Jogador\n"
        "q - Sair\n"
    )

    while True:
        print(menu)
        opcao = input("Opcao: ").strip().lower()

        if opcao == '1':
            jogo_humano_vs_computador()
        elif opcao == '2':
            jogo_humano_vs_humano()
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print("Opcao invalida. Tente de novo.")


if __name__ == "__main__":
    main()
