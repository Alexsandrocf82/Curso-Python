
# ============================================================
# EXERCÍCIO 066 - VÁRIOS NÚMEROS COM FLAG
# Curso: Python 3 - Mundo 2
# Professor: Gustavo Guanabara - Curso em Vídeo
# Conteúdo: Interrompendo repetições while
# Autor: Alexsandro Ferreira
# Versão: 1.0 - Implementação inicial
# Data de desenvolvimento: 18/11/2026
# Situação: Versão histórica com erro lógico identificado
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
# - Formatação de saída com f-strings
#
# OBSERVAÇÃO:
# Esta versão apresenta um erro lógico na contabilização
# e na soma dos números. Sua lógica inicial foi preservada
# para demonstrar a evolução do processo de aprendizagem.
# Código reconstruído a partir do histórico de acompanhamento.
# ============================================================

# Inicialização das variáveis de controle e acumulação.
numero = 0
soma = 0

# Estrutura de repetição contínua para entrada dos valores.
while True:

    # Recebe um número inteiro informado pelo usuário.
    numero = int(input('Digite um número inteiro (ou 999 para encerrar): '))

    # Verifica se o valor informado corresponde ao sentinela.
    # O comando break encerra imediatamente a repetição.
    if numero == 999:
        break

    # ERRO LÓGICO IDENTIFICADO:
    # A variável numero está sendo utilizada simultaneamente
    # para armazenar o valor informado e contabilizar entradas.
    # Esse incremento altera indevidamente o valor original.
    numero += 1

    # Acumula o valor já modificado pelo incremento anterior,
    # produzindo um resultado diferente da soma esperada.
    soma += numero

# Apresentação dos resultados.
# Nesta versão, a variável numero armazena o sentinela 999
# após o encerramento, e não a quantidade de entradas válidas.
print(f'A quantidade de números informados foi: {numero}')
print(f'A soma dos valores informados foi: {soma}')

# ============================================================
# ANÁLISE TÉCNICA DA VERSÃO 1.0
#
# Problemas identificados:
# 1. Ausência de uma variável exclusiva para o contador.
# 2. Alteração indevida do número informado pelo usuário.
# 3. Soma dos valores modificados em vez dos valores originais.
# 4. Apresentação do sentinela como quantidade de números.
#
# Exemplo de análise lógica:
# Entrada: 5, 8, 12, 999
# Resultado produzido: quantidade = 999; soma = 28.
# Resultado esperado: quantidade = 3; soma = 25.
#
# Aprendizado:
# Cada variável deve possuir uma responsabilidade claramente
# definida dentro do algoritmo.
#
# Os problemas identificados foram corrigidos na versão 2.0.
# ============================================================
