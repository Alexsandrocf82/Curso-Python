
# Projeto - Sistema de Cadastro | Versão 2
# Objetivo: realizar múltiplos cadastros com validação de dados
# e apresentar estatísticas gerais das pessoas cadastradas.
# Conceitos: while, if/elif/else, contadores, acumuladores
# e programação defensiva.


# Inicialização dos contadores e acumuladores
total_pessoas = 0
total_homens = 0
total_mulheres = 0
soma_idades = 0

continuar = 'S'


# Laço principal de cadastro
while continuar == 'S':

    # Entrada e validação do nome
    nome = input('Digite o nome: ').strip()

    while len(nome) == 0:
        print('Erro: nome não pode ser vazio ou conter apenas espaços.')
        nome = input('Digite um nome válido: ').strip()

    # Entrada e validação da idade
    entrada_idade = input('Digite a idade (entre 0 e 120): ').strip()

    while not entrada_idade.isdigit() or not (0 <= int(entrada_idade) <= 120):
        print('Erro: idade deve ser um número inteiro entre 0 e 120.')
        entrada_idade = input('Digite uma idade válida: ').strip()

    idade = int(entrada_idade)

    # Entrada e validação do sexo
    sexo = input('Digite o sexo (M/F): ').strip().upper()

    while sexo not in ['M', 'F']:
        print('Erro: Entrada inválida. Sexo deve ser "M" ou "F".')
        sexo = input('Digite o sexo (M/F): ').strip().upper()

    # Classificação por faixa etária
    if idade <= 11:
        faixa_etaria = 'Criança'
    elif idade <= 17:
        faixa_etaria = 'Adolescente'
    elif idade <= 59:
        faixa_etaria = 'Adulto'
    else:
        faixa_etaria = 'Idoso'

    # Identificação do sexo por extenso
    if sexo == 'M':
        sexo_extenso = 'Masculino'
    else:
        sexo_extenso = 'Feminino'

    # Exibição dos dados cadastrados
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Sexo: {sexo_extenso}')
    print(f'Faixa Etária: {faixa_etaria}')
    print('-' * 38)

    # Atualização dos contadores e acumuladores
    total_pessoas += 1
    soma_idades += idade

    if sexo == 'M':
        total_homens += 1
    else:
        total_mulheres += 1

    # Controle e validação de novos cadastros
    continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()

    while continuar not in ['S', 'N']:
        print('Erro: Responda apenas com "S" para Sim ou "N" para Não')
        continuar = input('Deseja cadastrar outra pessoa? [S/N]: ').strip().upper()


# Relatório estatístico final
print('=' * 30)
print('RESUMO DOS CADASTROS')
print('=' * 30)

# Programação defensiva: previne divisão por zero
# caso o fluxo do programa passe a permitir zero cadastros.
if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas

    print(f'Total de pessoas cadastradas: {total_pessoas}')
    print(f'Total de homens: {total_homens}')
    print(f'Total de mulheres: {total_mulheres}')
    print(f'Média de idade do grupo: {media_idade:.1f} anos')
else:
    print('Nenhuma pessoa foi cadastrada.')
