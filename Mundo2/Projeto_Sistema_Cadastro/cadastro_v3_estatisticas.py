
# Projeto  - Sistema de Cadastro | Versão 3
# Cadastro de pessoas com relatório estatístico por sexo e faixa etária.
# Conceitos: while, condicionais, validação, contadores e acumuladores.
# Programação defensiva: previne divisão por zero caso o fluxo do programa passe a permitir zero cadastros.

# Contadores e acumuladores
total_pessoas = 0
total_homens = 0
total_mulheres = 0
soma_idades = 0

total_criancas = 0
total_adolescentes = 0
total_adultos = 0
total_idosos = 0

continuar = 'S'

# Cadastro e validação dos dados
while continuar == 'S':
    nome = input('Digite o nome: ').strip()

    while len(nome) == 0:
        print('Erro: nome não pode ser vazio ou conter apenas espaços.')
        nome = input('Digite um nome válido: ').strip()

    entrada_idade = input('Digite a idade (entre 0 e 120): ').strip()

    while not entrada_idade.isdigit() or not (0 <= int(entrada_idade) <= 120):
        print('Erro: idade deve ser um número inteiro entre 0 e 120.')
        entrada_idade = input('Digite uma idade válida: ').strip()

    idade = int(entrada_idade)

    sexo = input('Digite o sexo (M/F): ').strip().upper()

    while sexo not in ['M', 'F']:
        print('Erro: Entrada inválida. Sexo deve ser "M" ou "F".')
        sexo = input('Digite o sexo (M/F): ').strip().upper()

    # Classificação e contagem por faixa etária
    if idade <= 11:
        faixa_etaria = 'Criança'
        total_criancas += 1
    elif idade <= 17:
        faixa_etaria = 'Adolescente'
        total_adolescentes += 1
    elif idade <= 59:
        faixa_etaria = 'Adulto'
        total_adultos += 1
    else:
        faixa_etaria = 'Idoso'
        total_idosos += 1

    if sexo == 'M':
        sexo_extenso = 'Masculino'
    else:
        sexo_extenso = 'Feminino'

    # Exibição do cadastro
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Sexo: {sexo_extenso}')
    print(f'Faixa Etária: {faixa_etaria}')
    print('-' * 38)

    # Atualização das estatísticas gerais
    total_pessoas += 1
    soma_idades += idade

    if sexo == 'M':
        total_homens += 1
    else:
        total_mulheres += 1

    # Controle de novos cadastros
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
    print('-' * 30)

    print('Distribuição por Faixa Etária:')
    print(f' - Crianças (0 a 11 anos): {total_criancas}')
    print(f' - Adolescentes (12 a 17 anos): {total_adolescentes}')
    print(f' - Adultos (18 a 59 anos): {total_adultos}')
    print(f' - Idosos (60+ anos): {total_idosos}')
else:
    print('Nenhuma pessoa foi cadastrada.')
