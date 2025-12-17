from logic.Moinho import *


def jogo_humano_vs_computador():
    # escolher peça do humano
    while True:
        escolha = input("Escolha o jogador humano (X/O): ").strip().upper()
        if escolha in ('X', 'O'):
            jogador_humano = f'[{escolha}]'
            break
        print("Escolha inválida. Introduza 'X' ou 'O'.")

    # escolher dificuldade
    niveis = {'1': 'facil', '2': 'normal', '3': 'dificil'}
    while True:
        escolha_n = input("Escolha a dificuldade do computador: 1-facil 2-normal 3-dificil: ").strip()
        if escolha_n in niveis:
            nivel = niveis[escolha_n]
            break
        print("Escolha inválida. Tente novamente.")

    vencedor = moinho(jogador_humano, nivel)
    print("Vencedor:", vencedor)


def jogo_humano_vs_humano():
    tabuleiro = cria_tabuleiro()
    peca_atual = cria_peca('X')

    while True:
        print(tabuleiro_para_str(tabuleiro))
        movimento = obter_movimento(tabuleiro, peca_atual)

        if len(movimento) == 1:
            coloca_peca(tabuleiro, peca_atual, movimento[0])
        else:
            move_peca(tabuleiro, movimento[0], movimento[1])

        ganhador = obter_ganhador(tabuleiro)
        if not pecas_iguais(ganhador, cria_peca(' ')):
            print(tabuleiro_para_str(tabuleiro))
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
        opcao = input("Opção: ").strip().lower()
        if opcao == '1':
            jogo_humano_vs_computador()
        elif opcao == '2':
            jogo_humano_vs_humano()
        elif opcao == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente de novo.")


if __name__ == "__main__":
    main()