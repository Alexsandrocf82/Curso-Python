'''Faça um programa que calcule a
soma entre todos os números impares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')

'''soma = 0
cont = 0
for c in range(3, 501, 6): # essa resolução é mais eficiente, pois já começa no primeiro número ímpar múltiplo de 3 e vai somando de 6 em 6, garantindo que todos os números sejam ímpares e múltiplos de 3.    
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')'''