
# ============================================================
# EXERCÍCIO 067 - TABUADA V3.0
# Curso: Python 3 - Mundo 2
# Professor: Gustavo Guanabara - Curso em Vídeo
# Conteúdo: Interrompendo repetições while
# Autor: Alexsandro Ferreira
# Versão do código: 1.0 - Implementação validada
# Data de validação: 18/11/2026
# Avaliação técnica: 10,0/10
# Situação: Versão final validada
# ============================================================
#
# OBJETIVO:
# Desenvolver um programa que apresente a tabuada de
# multiplicação de vários números inteiros informados pelo
# usuário, encerrando a execução quando for digitado um
# número negativo.
#
# CONCEITOS APLICADOS:
# - Estrutura de repetição while True
# - Estrutura de repetição for
# - Estruturas de repetição aninhadas
# - Estrutura condicional if
# - Interrupção de repetição com break
# - Função range()
# - Operadores relacionais
# - Operadores aritméticos
# - Formatação de saída com f-strings
#
# ESTRATÉGIA DE IMPLEMENTAÇÃO:
# A estrutura while controla a entrada contínua dos números,
# enquanto a estrutura for é responsável pela geração de
# cada tabuada. O comando break encerra o laço principal
# quando o usuário informa um valor negativo.
# ============================================================

# Estrutura principal de repetição para leitura dos números.
while True:

    # Recebe o número inteiro cuja tabuada será apresentada.
    numero = int(input('Digite um número inteiro: '))

    # Verifica a condição de encerramento do programa.
    # Qualquer número negativo interrompe o laço principal
    # antes que sua tabuada seja gerada.
    if numero < 0:
        break

    # Estrutura de repetição interna responsável por gerar
    # os multiplicadores de 1 a 10.
    # O limite superior da função range() não é incluído.
    for c in range(1, 11):

        # Calcula e apresenta cada operação de multiplicação.
        # A formatação :2 reserva duas posições para o
        # multiplicador, melhorando o alinhamento da saída.
        print(f'{numero} x {c:2} = {numero * c}')

# Mensagem apresentada somente após o encerramento
# da estrutura principal de repetição.
print('Programa encerrado ')

# ============================================================
# TESTES FUNCIONAIS REALIZADOS EM 18/11/2026
#
# Teste 01 - Número positivo:
# Entrada: 5, -1
# Resultado: tabuada de 5, com 10 operações, e encerramento.
# Situação: APROVADO.
#
# Teste 02 - Encerramento imediato:
# Entrada: -3
# Resultado: encerramento sem exibir nenhuma tabuada.
# Situação: APROVADO.
#
# Teste 03 - Número zero:
# Entrada: 0, -1
# Resultado: tabuada de zero, com 10 produtos iguais a zero.
# Situação: APROVADO.
#
# Teste 04 - Múltiplas tabuadas:
# Entrada: 2, 7, 10, -5
# Resultado: três tabuadas, totalizando 30 operações.
# Situação: APROVADO.
#
# Resultado geral: 4 de 4 testes aprovados.
# Aproveitamento: 100%.
#
# LIMITAÇÕES:
# O programa pressupõe que o usuário informe números inteiros.
# O tratamento de entradas não numéricas está fora do escopo
# original do exercício.
# ============================================================
