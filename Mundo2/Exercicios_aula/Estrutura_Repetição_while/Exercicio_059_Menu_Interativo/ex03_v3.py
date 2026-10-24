
# Exercício 059 - Menu Interativo | Versão 3
# Curso de Python - Mundo 2 | Professor Gustavo Guanabara
# Objetivo: realizar operações com validação da opção do menu.
# Conceitos: while, if/elif/else, operadores aritméticos,time.sleep() e isdigit()


# Entrada dos valores
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opcao = 0

# Menu principal
while opcao != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')

    # Validação da opção antes da conversão para inteiro
    entrada = input('Digite a opção desejada: ').strip()

    if entrada.isdigit():
        opcao = int(entrada)
    else:
        opcao = 0

    # Operações disponíveis
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')

    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicacao}')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior número é : {maior}')
        elif n2 > n1:
            maior = n2
            print(f'O maior número é : {maior}')
        else:
            print('Os números são iguais')

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção Inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)

print('Fim do Programa. Volte Sempre!')
