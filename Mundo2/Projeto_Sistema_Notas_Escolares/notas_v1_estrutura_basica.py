
# ==========================================================
# PROJETO 08 - SISTEMA DE CONTROLE DE NOTAS ESCOLARES
# Versão: 1.0 - Estrutura básica
# Desenvolvimento original: 08/11/2026
# Linguagem: Python 3
#
# Objetivo:
# Cadastrar alunos, calcular médias individuais, classificar
# o desempenho escolar e calcular a média geral da turma.
#
# Conceitos aplicados:
# - Estruturas condicionais (if, elif e else)
# - Estrutura de repetição (while)
# - Contadores e acumuladores
# - Operadores aritméticos e relacionais
# - Formatação de strings
# ==========================================================

# Inicialização das variáveis de controle
contador_alunos = 0
soma_medias = 0
continuar = 'S'

# Laço principal de cadastramento dos alunos
while continuar.upper() == 'S':

    # Entrada de dados do aluno
    nome_aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    # Cálculo da média individual
    media = (nota1 + nota2) / 2

    # Classificação do desempenho escolar
    if media >= 7:
        situacao = 'Aprovado'
    elif media >= 5:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    # Exibição do resultado individual
    print(f'Aluno: {nome_aluno}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')

    # Atualização do contador e do acumulador
    contador_alunos += 1
    soma_medias += media

    # Controle de continuidade do cadastramento
    continuar = input(
        'Deseja cadastrar outro aluno? (S/N): '
    ).strip().upper()

# Cálculo da média geral e proteção contra divisão por zero
if contador_alunos > 0:
    media_geral = soma_medias / contador_alunos

    # Exibição do relatório final da turma
    print(f'Total de alunos cadastrados: {contador_alunos}')
    print(f'Média geral da turma: {media_geral:.2f}')
else:
    print('Nenhum aluno cadastrado.')

# Encerramento do programa
print('\nPrograma encerrado.')

