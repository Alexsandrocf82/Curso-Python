'''Sistema de Cadastro Simples (duas versões)

O programa cadastra pessoas com os mesmos dados nas duas versões. O que muda é a forma de tratar o erro e de repetir.

Dados e regras de validação (valem para as duas versões)

O programa lê:

nome: não pode ficar vazio. Um nome só com espaços também é inválido.
idade: número inteiro de 0 a 120 (inclusive).
sexo: somente M ou F. Minúsculas e espaços sobrando devem ser aceitos.
Faixa etária (calculada a partir da idade)
De 0 a 11 anos: Criança
De 12 a 17 anos: Adolescente
De 18 a 59 anos: Adulto
A partir de 60 anos: Idoso'''

nome = str(input('Digite seu nome: ')).strip()
if nome == '':
    print('Nome inválido. Digite novamente.')
    nome = str(input('Digite seu nome: ')).strip()

idade = int(input('Digite sua idade: '))
if idade < 0 or idade > 120:
    print('Idade inválida. Digite novamente.')
    idade = int(input('Digite sua idade: '))

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
if sexo != 'M' and sexo != 'F':
    print('Sexo inválido. Digite M ou F.')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

nome_valido = (nome != '')
idade_valida = (idade >= 0 and idade <= 120)
sexo_valido = (sexo == 'M' or sexo == 'F')

if nome_valido and idade_valida and sexo_valido:
    if sexo == 'M':
        sexo_extenso = 'Masculino'
    else:
        sexo_extenso = 'Feminino'

    if idade <= 11:
        faixa_etaria = 'Criança'
    elif idade <= 17:
        faixa_etaria = 'Adolescente'
    elif idade <= 59:
        faixa_etaria = 'Adulto'
    else:
        faixa_etaria = 'Idoso'

    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Sexo: {sexo_extenso}')
    print(f'Faixa Etária: {faixa_etaria}')
else:
    print('Cadastro não concluído.')
    if not nome_valido:
        print('Nome inválido.')
    if not idade_valida:
        print('Idade inválida.')
    if not sexo_valido:
        print('Sexo inválido.')