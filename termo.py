import random

def carregar_base_palavras() -> list:
    """
    Retorna uma lista de palavras com 5 caracteres.
    Return: list
    """
    return [
        'TERMO', 'LIVRO', 'TESTE', 'PORTA', 'FICAR', 
        'CHAVE', 'TEMPO', 'MUNDO', 'NOITE', 'CARRO', 
        'FESTA', 'SORTE', 'FORTE', 'CINCO', 'LETRA', 
        'REGRA', 'FALAR', 'ANDAR', 'COMER', 'JUSTO'
    ]

def sortear_palavra(base_palavras: list) -> list:
    """
    Sorteia uma palavra aleatória e armazena cada letra em uma lista.
    Param: base_palavras: list
    Return: list
    """
    palavra_sorteada = random.choice(base_palavras)
    
    letras_da_palavra = []
    for letra in palavra_sorteada:
        letras_da_palavra.append(letra)
        
    return letras_da_palavra

def criar_matriz(n_linhas: int, n_colunas: int, padrao: str) -> list:
    """
    Cria uma matriz bidimensional NxM para o tabuleiro.
    Param: n_linhas: int, n_colunas: int, padrao: str
    Return: list
    """
    matriz = [] 
    for i in range(n_linhas):
        linha = [] 
        for j in range(n_colunas):
            linha.append(padrao)
        matriz.append(linha)
    return matriz

def mostrar_tabuleiro(matriz_armazenamento: list, matriz_espelho: list, tentativa_atual: int) -> None:
    """
    Imprime as linhas do tabuleiro jogadas até a tentativa atual.
    """
    print('\n --- ESTADO DO TABULEIRO ---')
    for linha in range(tentativa_atual + 1):
        print(f'Tentativa {linha + 1}:')
        print(f'Palavra: {matriz_armazenamento[linha]}')
        print(f'Status : {matriz_espelho[linha]}\n')

def jogar_termo():
    """
    Orquestra as regras do jogo, interação e tratamento de erros (try-except-else-finally).
    """
    tamanho_palavra = 5
    max_tentativas = 6

    print(' -- BEM-VINDO AO JOGO TERMO -- \n')
    print(f'Você tem {max_tentativas} tentativas para adivinhar a palavra.\n')
    print('Instruções da Matriz Espelho:')
    print('[C] = Letra Correta (Posição certa)')
    print('[E] = Letra Existe (Posição errada)')
    print('[X] = Letra Errada (Não existe)\n')

    base = carregar_base_palavras()
    palavra_alvo = sortear_palavra(base)
    
    # Matrizes que controlam o jogo
    matriz_armazenamento = criar_matriz(max_tentativas, tamanho_palavra, '_')
    matriz_espelho = criar_matriz(max_tentativas, tamanho_palavra, '_')
    
    tentativa_atual = 0
    vitoria = False

    # Laço principal do jogo
    while tentativa_atual < max_tentativas and vitoria == False:
        try:
            palpite = input(f'Digite uma palavra de {tamanho_palavra} letras (EM MAIÚSCULO): ')
            
            # Validação física de entrada
            if len(palpite) != tamanho_palavra:
                raise ValueError(f'A palavra deve ter exatamente {tamanho_palavra} caracteres.')
                
        except ValueError as erro:
            print(f'\n[ERRO DE ENTRADA]: {erro}')
            print('Digite novamente!\n')
            
        else:
            # O bloco else executa a lógica apenas se não houver erros na entrada
            letras_corretas = 0
            
            for i in range(tamanho_palavra):
                letra_atual = palpite[i]
                
                matriz_armazenamento[tentativa_atual][i] = letra_atual
                
                # Regras de validação do Termo
                if letra_atual == palavra_alvo[i]:
                    matriz_espelho[tentativa_atual][i] = '[C]'
                    letras_corretas += 1
                elif letra_atual in palavra_alvo:
                    matriz_espelho[tentativa_atual][i] = '[E]'
                else:
                    matriz_espelho[tentativa_atual][i] = '[X]'
            
            mostrar_tabuleiro(matriz_armazenamento, matriz_espelho, tentativa_atual)
            
            # Checagem de fim de jogo
            if letras_corretas == tamanho_palavra:
                vitoria = True
            else:
                tentativa_atual += 1
                
        finally:
            # O finally indica o término do processamento da rodada
            print(f'--- Fim do processamento da Tentativa ---')

    # Resultados finais fora do laço
    if vitoria == True:
        print(f'\n[SUCESSO]: Você venceu o jogo na tentativa {tentativa_atual + 1}!')
    else:
        palavra_correta = ""
        for letra in palavra_alvo:
            palavra_correta += letra
        print(f'\n[DERROTA]: Você perdeu! A palavra correta era {palavra_correta}')
        
    print('--- Encerrando a partida ---\n')

# (main)
while True:
    jogar_termo()
    
    opcao = input('Deseja jogar novamente? (1 - Sim / 2 - Sair): ')
    if opcao == '2':
        print('\nPrograma encerrado!')
        break
