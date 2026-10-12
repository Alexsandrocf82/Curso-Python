'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.'''
soma_idades = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menores_20 = 0

for c in range(1, 5):
    print(f'--- {c}ª pessoa ---')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').upper()

    soma_idades = soma_idades + idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
       idade_homem_mais_velho = idade
       nome_homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
       mulheres_menores_20 = mulheres_menores_20 + 1

media_idades = soma_idades / 4

print(f'A média de idade do grupo é de {media_idades}')
print(f'O homem mais velho é {nome_homem_mais_velho}, com a idade de {idade_homem_mais_velho}')
print(f'Ao todo, {mulheres_menores_20} mulheres têm menos de 20 anos')