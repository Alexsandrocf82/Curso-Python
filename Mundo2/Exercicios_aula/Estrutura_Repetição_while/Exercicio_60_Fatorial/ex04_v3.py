entrada = input('Digite um número inteiro:')
if entrada.isdigit():
    numero = int(entrada)
    contador = numero
    fatorial = 1
    while contador > 0:
        fatorial *= contador
        contador -= 1
    print(f'O fatorial de {numero} é {fatorial}')
else:
    print('Erro! Digite apenas números inteiros não negativos.')
