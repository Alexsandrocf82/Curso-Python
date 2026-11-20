# ============================================================
# Exercício 064 - Tratando Vários Valores
# Curso: Python 3 - Mundo 2 | Curso em Vídeo
# Professor: Gustavo Guanabara
# Autor: Alexsandro Ferreira
# Versão: 1.0
# Validação: 20/11/2026
# ============================================================
# Objetivo:
# Ler vários números inteiros, contabilizar a quantidade
# de valores informados e calcular a soma entre eles.
#
# O programa encerra quando o usuário informa o valor 999,
# que não deve ser incluído na contagem nem na soma.
# ============================================================

# Inicialização do contador e do acumulador
contador_numeros = 0
soma_numeros = 0

# Leitura inicial para permitir a verificação da condição do laço
numero = int(input('Digite um número inteiro: '))

# Estrutura de repetição controlada pelo valor sentinela 999.
# Enquanto o número informado for diferente de 999,
# o programa continuará processando os valores.
while numero != 999:

    # Atualização da quantidade de números válidos informados
    contador_numeros += 1

    # Acumulação dos valores digitados pelo usuário
    soma_numeros += numero

    # Leitura de um novo número para atualizar a condição do laço
    numero = int(input('Digite um número inteiro: '))

# Apresentação dos resultados após o encerramento da repetição.
# O valor sentinela 999 não participa dos resultados.
print(f'A quantidade de números digitados foi: {contador_numeros}')
print(f'A soma dos números digitados é: {soma_numeros}')