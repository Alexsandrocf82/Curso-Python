
# Exercício 068 - Jogo do Par ou Ímpar
# Versão 1 - Implementação inicial do jogo
# Curso em Vídeo - Python 3 - Mundo 2

# Importação da função para geração de números aleatórios
from random import randint

# Inicialização do contador de vitórias consecutivas
vitorias = 0

# Laço principal do jogo
while True:
    print('==' * 10)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('==' * 10)

    # Entrada de dados do jogador
    numero_jogador = int(input('Digite um número: '))
    escolha_jogador = input('Par ou Impar[P/I]: ').strip().upper()

    # Validação da escolha entre par e ímpar
    if escolha_jogador != 'P' and escolha_jogador != 'I':
        print('Opção inválida. Tente novamente.')
        continue

    # Sorteio do número do computador e cálculo da soma
    numero_computador = randint(0, 10)
    soma = numero_jogador + numero_computador

    # Verificação se o resultado da soma é par
    if soma % 2 == 0:
        resultado = 'PAR'

        # Vitória do jogador
        if escolha_jogador == 'P':
            print('==' * 10)
            print(f'Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} deu {resultado}')
            print('==' * 10)
            print('Você Venceu!')
            print('==' * 10)
            vitorias += 1

        # Derrota do jogador e encerramento do laço
        elif escolha_jogador == 'I':
            print('==' * 10)
            print(f'Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} deu {resultado}')
            print('==' * 10)
            print('Você Perdeu!')
            print('==' * 10)
            break

        else:
            print('Opção inválida. Tente novamente.')

    # Tratamento do resultado ímpar
    else:
        resultado = 'IMPAR'

        # Vitória do jogador
        if escolha_jogador == 'I':
            print('==' * 10)
            print(f'Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} deu {resultado}')
            print('==' * 10)
            print('Você Venceu!')
            print('==' * 10)
            vitorias += 1

        # Derrota do jogador e encerramento do laço
        elif escolha_jogador == 'P':
            print('==' * 10)
            print(f'Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} deu {resultado}')
            print('==' * 10)
            print('Você Perdeu')
            print('==' * 10)
            break

        else:
            print('Opção Inválida. Tente novamente.')

# Exibição do total de vitórias consecutivas
print(f'GAME OVER! Você venceu {vitorias} vezes.')
