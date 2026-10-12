'''faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e qual foi o menor peso lido.'''

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior:.1f}Kg')
print(f'O menor peso lido foi {menor:.1f}Kg')
