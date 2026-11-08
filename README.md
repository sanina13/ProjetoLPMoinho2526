# Jogo do Moinho

Implementação em Python do **Jogo do Moinho** (variante 3×3, com diagonais) para jogar no terminal. Projeto académico (IPBeja, 2025/26).

Joga-se contra o computador (3 níveis de dificuldade) ou contra outro jogador.

## O tabuleiro

```
   a   b   c
1 [ ]-[ ]-[ ]
   | \ | / |
2 [ ]-[ ]-[ ]
   | / | \ |
3 [ ]-[ ]-[ ]
```

As posições são identificadas por **coluna + linha** (`a1`, `b2`, `c3`, ...).

## Regras

1. **X joga sempre primeiro.**
2. **Fase de colocação:** enquanto um jogador tiver menos de 3 peças no tabuleiro, escolhe uma posição livre para colocar uma peça (ex.: `b2`).
3. **Fase de movimentação:** com as 3 peças colocadas, cada jogada move uma peça para uma posição **adjacente livre** (ex.: `a1b2` move a peça de `a1` para `b2`). A adjacência segue as linhas e diagonais desenhadas.
4. **Passar a vez:** se nenhuma das tuas peças se puder mover, indicas a mesma posição como origem e destino (ex.: `a1a1`).
5. **Vitória:** ganha quem formar um **moinho** (3 peças suas alinhadas numa linha ou coluna).

## Como jogar

Requisitos: Python 3.

```bash
git clone https://github.com/sanina13/ProjetoLPMoinho2526.git
cd ProjetoLPMoinho2526
python main.py
```

Menu principal:

```
1 - Jogador (X/O) vs Computador
2 - Jogador vs Jogador
q - Sair
```

No modo contra o computador escolhes a peça (`X` ou `O`) e a dificuldade:

| Nível | Comportamento |
|-------|---------------|
| 1 – fácil | Escolhe o primeiro movimento possível, sem previsão de jogadas |
| 2 – normal | Minimax com profundidade 1 |
| 3 – difícil | Minimax com profundidade 5 |

Na fase de colocação, o computador tenta ganhar de imediato e bloquear o adversário.

## Estrutura do projeto

```
.
├── main.py              # Menu e ciclos de jogo (humano vs computador / humano vs humano)
├── logic/
│   ├── Moinho.py        # Função moinho(): jogo completo contra o computador
│   └── Movimentos.py    # Movimentos manuais e automáticos, avaliação e minimax
├── models/
│   ├── Peca.py          # TAD peça
│   ├── Posicao.py       # TAD posição
│   └── Tabuleiro.py     # TAD tabuleiro
├── public_tests.py      # Testes públicos
└── LICENSE
```

O código está organizado em **tipos abstratos de dados** (peça, posição e tabuleiro), com construtores, seletores, reconhecedores, testes e transformadores, e a lógica do jogo construída por cima.

## Testes

```bash
python public_tests.py
```

## Licença

Distribuído sob a licença MIT. Ver [LICENSE](LICENSE).

## Autor

Tiago Sanina, [@sanina13](https://github.com/sanina13)
