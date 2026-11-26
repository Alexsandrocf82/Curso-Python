# Exercício 069 - Análise de Dados do Grupo
# Curso em Vídeo - Python 3 - Mundo 2
# Versão 2 - Validação de dados e melhoria da interface
# Autor: Alexsandro Ferreira

# Inicialização dos contadores
pessoas_mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

# Cabeçalho principal do sistema
# O método center() centraliza o texto em 50 caracteres
print('=' * 50)
print('SISTEMA DE CADASTRO DE PESSOAS'.center(50))
print('=' * 50)

# Laço principal responsável pelo cadastro das pessoas
while True:

    # Cabeçalho de identificação do cadastro
    print('-' * 50)
    print('CADASTRO DE PESSOA'.center(50))
    print('-' * 50)

    # Recebe a idade inicialmente como string
    # O método strip() remove espaços nas extremidades
    idade = input('Digite a idade da pessoa: ').strip()

    # Validação da entrada numérica
    # Rejeita letras, entradas vazias, números decimais
    # e números negativos nos formatos usuais
    if not idade.isdigit():
        print('Entrada Inválida. Digite um número inteiro não negativo')

        # Reinicia o laço sem processar o cadastro inválido
        continue

    # Converte a idade para inteiro após a validação
    idade = int(idade)

    # Solicita o sexo da pessoa
    # O método upper() converte a entrada para maiúsculas
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()

    # Validação do sexo informado
    while sexo != 'M' and sexo != 'F':
        print('Opção inválida. Tente novamente.')
        sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()

    # Contabiliza as pessoas com idade superior a 18 anos
    if idade > 18:
        pessoas_mais_de_18 += 1

    # Contabiliza todos os homens cadastrados,
    # independentemente da idade
    if sexo == 'M':
        homens_cadastrados += 1

    # Contabiliza as mulheres com idade inferior a 20 anos
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    # Solicita ao usuário a continuidade do cadastro
    continuar = input('Deseja continuar cadastrando pessoas? [S/N]: ').strip().upper()

    # Validação da opção de continuidade
    while continuar != 'S' and continuar != 'N':
        print('Opção inválida. Tente novamente.')
        continuar = input('Deseja continuar cadastrando pessoas? [S/N]: ').strip().upper()

    # Encerra o laço principal quando o usuário digitar N
    if continuar == 'N':
        break

# Cabeçalho do relatório final
print('=' * 50)
print('RELATÓRIO FINAL'.center(50))
print('=' * 50)

# Apresentação dos resultados consolidados
print(f'Quantidade de pessoas com mais de 18 anos: {pessoas_mais_de_18}')
print(f'Quantidade de homens cadastrados: {homens_cadastrados}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}')

# Mensagem de encerramento do sistema
print('=' * 50)
print('SISTEMA ENCERRADO'.center(50))
print('=' * 50)