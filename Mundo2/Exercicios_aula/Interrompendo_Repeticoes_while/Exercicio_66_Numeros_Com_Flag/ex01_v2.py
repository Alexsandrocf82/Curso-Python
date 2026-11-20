
# ============================================================
# EXERCÍCIO 066 - VÁRIOS NÚMEROS COM FLAG
# Curso: Python 3 - Mundo 2
# Professor: Gustavo Guanabara - Curso em Vídeo
# Conteúdo: Interrompendo repetições while
# Autor: Alexsandro Ferreira
# Versão: 2.0 - Correção e validação funcional
# Data de validação: 18/11/2026
# Avaliação técnica: 10,0/10
# Situação: Versão final validada
# ============================================================
#
# OBJETIVO:
# Desenvolver um programa que leia vários números inteiros,
# utilizando o valor 999 como sentinela para encerrar a
# repetição. Ao final, apresentar a quantidade e a soma
# dos valores informados, desconsiderando o sentinela.
#
# CONCEITOS APLICADOS:
# - Estrutura de repetição while True
# - Estrutura condicional if
# - Interrupção de repetição com break
# - Utilização de valor sentinela (flag)
# - Contadores e acumuladores
# - Separação das responsabilidades das variáveis
# - Formatação de saída com f-strings
#
# EVOLUÇÃO EM RELAÇÃO À VERSÃO 1.0:
# Criação de uma variável exclusiva para contabilizar os
# números informados, preservando o valor original de cada
# entrada e garantindo a precisão da soma acumulada.
# ============================================================

# Inicialização do contador de números válidos.
numeros_digitados = 0

# Inicialização do acumulador responsável pela soma.
soma = 0

# Estrutura de repetição contínua, encerrada pelo sentinela.
while True:

    # Recebe um número inteiro informado pelo usuário.
    numero = int(input('Digite um número inteiro (ou 999 para encerrar): '))

    # Verifica se o usuário informou o valor sentinela.
    # A interrupção ocorre antes da contagem e da soma,
    # impedindo que o valor 999 participe dos resultados.
    if numero == 999:
        break

    # Incrementa o contador a cada entrada válida.
    numeros_digitados += 1

    # Adiciona o valor original informado ao acumulador.
    soma += numero

# Apresentação do relatório final após o encerramento do laço.
print(f'A quantidade de números informados foi: {numeros_digitados}')
print(f'A soma dos valores informados foi: {soma}')

# ============================================================
# TESTES FUNCIONAIS REALIZADOS EM 18/11/2026
#
# Teste 01 - Sequência de números positivos:
# Entrada: 5, 8, 12, 999
# Resultado: quantidade = 3; soma = 25.
# Situação: APROVADO.
#
# Teste 02 - Encerramento imediato:
# Entrada: 999
# Resultado: quantidade = 0; soma = 0.
# Situação: APROVADO.
#
# Teste 03 - Números positivos, negativos e zero:
# Entrada: 10, -5, 0, 15, 999
# Resultado: quantidade = 4; soma = 20.
# Situação: APROVADO.
#
# Teste 04 - Valores próximos ao sentinela:
# Entrada: 998, 1000, 999
# Resultado: quantidade = 2; soma = 1998.
# Situação: APROVADO.
#
# Resultado geral: 4 de 4 testes aprovados.
# Aproveitamento: 100%.
#
# LIMITAÇÕES:
# O programa pressupõe que o usuário informe números inteiros.
# Entradas não numéricas não possuem tratamento de exceções,
# funcionalidade que está fora do escopo original do exercício.
# ============================================================
