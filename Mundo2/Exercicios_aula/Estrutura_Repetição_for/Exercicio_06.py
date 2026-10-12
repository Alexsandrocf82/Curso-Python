'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite  a razão da PA: '))
for c in range(0, 10):
    termo = primeiro_termo + (c * razao)
    print(f'{termo}', end=' ')


    # resolução do professor :
'''primeiro  = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão # aqui o professor calcula o décimo termo da PA
for c in range(primeiro, decimo + razão, razão): # Aqui ele faz o loop do primeiro termo até o décimo termo, acrescentando a razão a cada iteração
    print(f'{c}' , end=' ')'''