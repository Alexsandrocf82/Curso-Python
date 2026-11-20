# ============================================================
# Exercício 065 - Maior e Menor Valores
# Curso: Python 3 - Mundo 2 | Curso em Vídeo
# Professor: Gustavo Guanabara
# Autor: Alexsandro Ferreira
# Versão: 1.0
# Validação: 20/11/2026
# ============================================================
# Objetivo:
# Ler vários números inteiros, calcular a média aritmética
# e identificar o maior e o menor valor informado.
#
# O usuário pode decidir se deseja continuar ou encerrar
# a entrada de dados por meio das opções S/N.
#
# Implementação complementar:
# Apresentar a soma total dos números digitados,
# ampliando os requisitos do enunciado original.
# ============================================================

# Inicialização do contador e do acumulador
total_numeros = 0
soma = 0

# Variável de controle da estrutura de repetição.
# O valor inicial S garante a primeira execução do laço.
continuar = 'S'

# Estrutura de repetição controlada pela escolha do usuário
while continuar == 'S':

    # Entrada de dados
    numero = int(input('Digite um número inteiro: '))

    # Atualização do contador e do acumulador
    total_numeros += 1
    soma += numero

    # Inicialização dos valores de referência.
    # O primeiro número informado é considerado inicialmente
    # tanto o maior quanto o menor valor.
    # Essa estratégia permite trabalhar também com negativos.
    if total_numeros == 1:
        numero_maior = numero
        numero_menor = numero

    # Comparação dos próximos números com os valores
    # de referência armazenados anteriormente.
    else:

        # Atualização do maior valor, quando necessário
        if numero > numero_maior:
            numero_maior = numero

        # Atualização do menor valor, quando necessário
        if numero < numero_menor:
            numero_menor = numero

    # Controle de continuidade do programa.
    # strip() remove espaços nas extremidades da entrada.
    # upper() converte a resposta para letras maiúsculas.
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()

# Cálculo da média após o encerramento da repetição.
# A soma acumulada é dividida pela quantidade de números.
media = soma / total_numeros

# Apresentação dos resultados solicitados no enunciado original
print(f'A média dos números digitado é: {media:.2f}')
print(f'O maior número digitado foi: {numero_maior}')
print(f'O menor número digitado foi: {numero_menor}')

# Implementação complementar ao enunciado original:
# apresentação da soma total dos números informados.
print(f'A soma dos numero digitados foi: {soma}')