# Termo em Python

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white) ![Projeto acadêmico](https://img.shields.io/badge/Projeto-acad%C3%AAmico-6D28D9)

**Cinco letras. Seis tentativas. Um desafio de lógica no terminal.**

Jogo de adivinhação de palavras inspirado no Termo, desenvolvido por **Leticia Felix** como projeto acadêmico. A proposta é aplicar fundamentos de programação em Python em uma experiência interativa: a cada palpite, o jogador recebe indicações sobre as letras e suas posições.

## Objetivo

Praticar decomposição de problemas em funções, manipulação de listas e matrizes, estruturas de controle e tratamento de exceções. O código mantém uma abordagem didática, com etapas explícitas para construção do tabuleiro e avaliação das tentativas.

## Como funciona

1. O programa sorteia uma palavra de cinco letras entre 20 opções predefinidas.
2. O jogador digita um palpite de cinco caracteres **em maiúsculas**.
3. Duas matrizes de 6 × 5 registram os palpites e os resultados de cada letra.
4. O tabuleiro exibe o histórico das tentativas e suas indicações:

| Indicação | Significado |
| :---: | --- |
| `[C]` | Letra correta na posição certa. |
| `[E]` | A letra existe na palavra, mas está em outra posição. |
| `[X]` | A letra não existe na palavra. |

O jogador vence ao acertar a palavra inteira. Após seis palpites sem acerto, o jogo revela a resposta. Ao final, digite `1` para jogar novamente ou `2` para sair.

### Exemplo de uma rodada

Considerando a palavra secreta `TERMO` e o palpite `TEMPO`, o resultado é:

```text
Tentativa 1:
Palavra: ['T', 'E', 'M', 'P', 'O']
Status : ['[C]', '[C]', '[E]', '[X]', '[C]']
```

## Funcionalidades

- Sorteio de palavras com `random.choice`, da biblioteca padrão.
- Limite de seis tentativas por partida.
- Histórico de palpites e retorno individual por letra.
- Validação do tamanho da entrada: palpites com tamanho diferente de cinco não consomem uma tentativa.
- Mensagens de vitória, derrota e encerramento.
- Opção de iniciar outra partida sem reiniciar o programa.
- Execução no terminal, sem dependências externas.

## Conceitos Python aplicados

| Conceito | Aplicação no projeto |
| --- | --- |
| Funções | Separação entre base de palavras, sorteio, criação de matrizes, exibição e fluxo da partida. |
| Listas e matrizes | Armazenamento das letras e dos estados do tabuleiro em listas aninhadas. |
| Laços `for` e `while` | Construção das matrizes, comparação das letras e repetição de partidas. |
| Condicionais e operadores | Classificação das letras e controle de vitória e tentativas. |
| Strings e indexação | Leitura dos palpites e acesso às posições de cada letra. |
| Exceções | Uso de `raise ValueError` e `try / except / else / finally` na validação da entrada. |
| Biblioteca padrão | Seleção aleatória com o módulo `random`. |
| Documentação | Docstrings, comentários e anotações de tipo em funções auxiliares. |

## Como executar

**Pré-requisito:** Python 3.6 ou superior, devido ao uso de f-strings. Utilize uma versão atual do Python 3.

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/LeticiaFelix18/jogo-termo-python.git
cd jogo-termo-python
```

Execute:

```bash
python termo.py
```

No Windows, também é possível usar `py termo.py`. Em sistemas que utilizam o comando `python3`, execute `python3 termo.py`.

Você também pode baixar o projeto em **Code → Download ZIP**, extrair a pasta e abrir um terminal nela. Não é necessário instalar pacotes com `pip`.

## Estrutura do projeto

```text
jogo-termo-python/
├── termo.py       # Código do jogo e interação pelo terminal
├── README.md      # Apresentação e instruções de uso
└── .gitignore     # Exclusão de arquivos locais e gerados pelo Python
```

## Escopo acadêmico

Esta versão preserva a lógica original do projeto. A validação verifica o tamanho da entrada; não consulta um dicionário, não restringe a entrada a letras e não converte minúsculas automaticamente. Por isso, siga a orientação de digitar palavras em maiúsculas.

A análise de letras repetidas considera a presença da letra na palavra, sem controlar a quantidade de ocorrências. Trata-se de uma regra simplificada em relação ao Termo original. Na opção de repetir, somente `2` encerra o programa; qualquer outra entrada inicia uma nova partida.

## Autoria

Desenvolvido por **Leticia Felix**.

[Conheça meu perfil no GitHub →](https://github.com/LeticiaFelix18)