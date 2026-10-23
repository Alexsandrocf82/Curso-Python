
# Projeto - Sistema de Cadastro | Versão 1
# Cadastro individual com validação de dados e classificação etária.
# Conceitos: variáveis, entrada de dados e estruturas condicionais.

# Entrada e validação do nome
nome = input('Digite o nome: ').strip()
nome_valido = len(nome) > 0

if not nome_valido:
    print('Erro: nome não pode ser vazio ou conter apenas espaços.')
    nome = input('Digite um nome válido: ').strip()
    nome_valido = len(nome) > 0

# Entrada e validação da idade
idade = int(input('Digite a idade (entre 0 e 120): '))
idade_valida = 0 <= idade <= 120

if not idade_valida:
    print('Erro: idade deve estar entre 0 e 120.')
    idade = int(input('Digite uma idade válida: '))
    idade_valida = 0 <= idade <= 120

# Entrada e validação do sexo
sexo = input('Digite o sexo (M/F): ').strip().upper()
sexo_valido = sexo in ['M', 'F']

if not sexo_valido:
    print('Erro: sexo deve ser M ou F.')
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    sexo_valido = sexo in ['M', 'F']

# Classificação etária e apresentação do cadastro
if nome_valido and idade_valida and sexo_valido:
    if idade <= 11:
        faixa_etaria = 'Criança'
    elif idade <= 17:
        faixa_etaria = 'Adolescente'
    elif idade <= 59:
        faixa_etaria = 'Adulto'
    else:
        faixa_etaria = 'Idoso'

    if sexo == 'M':
        sexo_extenso = 'Masculino'
    else:
        sexo_extenso = 'Feminino'

    print('-' * 38)
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Sexo: {sexo_extenso}')
    print(f'Faixa Etária: {faixa_etaria}')
else:
    print('Cadastro não realizado. Dados inválidos.')

