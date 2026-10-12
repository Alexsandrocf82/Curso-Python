''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date # biblioteca para pegar o ano atual

ano_atual = date.today().year
maioridade = 0
menoridade = 0 

for c in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento {c}:'))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'Ao todo tivemos {maioridade} pessoa(s) maiores de idade e {menoridade} pessoa(s) menores de idade.')

