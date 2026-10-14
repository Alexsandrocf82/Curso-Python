'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')


'''
Outra Forma de Resolver
2) Com [0] e not in 'MF' (versão do professor):
sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
Atenção: o [0] quebra com Enter vazio (IndexError) e aceita 'Mulher' como 'M'.
'''