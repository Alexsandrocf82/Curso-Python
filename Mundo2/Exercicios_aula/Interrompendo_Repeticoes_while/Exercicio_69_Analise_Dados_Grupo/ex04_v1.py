# Exercício 069 - Análise de Dados do Grupo
# Curso em Vídeo - Python 3 - Mundo 2
# Versão 1 - Implementação inicial
# Autor: Alexsandro Ferreira

# Inicialização dos contadores
pessoas_mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_20 = 0

# Laço principal responsável pelo cadastro das pessoas
while True:

    # Entrada dos dados da pessoa
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa [M/F]: ').strip().upper()

    # Validação do sexo informado
    # Repete a solicitação enquanto a opção for inválida
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

# Apresentação dos resultados após o encerramento do cadastro
print(f'Quantidade de pessoas com mais de 18 anos:{pessoas_mais_de_18}')
print(f'Quantidade de homens cadastrados:{homens_cadastrados}')
print(f'Quantidade de mulheres com menos de 20 anos:{mulheres_menos_20}')

    




    

    

