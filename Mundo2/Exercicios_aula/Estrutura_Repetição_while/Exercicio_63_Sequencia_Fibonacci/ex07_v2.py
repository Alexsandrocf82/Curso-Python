
# Exercício 63 - Sequência de Fibonacci
# Versão 2: solução com validação da quantidade de termos.

# Entrada de dados
quantidade = int(input('Digite a quantidade de termos que deseja mostrar: '))

# Verifica se a quantidade informada é válida
if quantidade <= 0:
    print('Quantidade inválida. Deve ser um número positivo.')

else:
    # Inicialização das variáveis da sequência
    anterior = 0
    atual = 1
    contador = 1

    # Apresenta os termos enquanto o contador não ultrapassar
    # a quantidade solicitada pelo usuário
    while contador <= quantidade:
        # Exibe o termo atual
        print(anterior, end=' -> ')

        # Calcula o próximo termo da sequência
        proximo = anterior + atual

        # Atualiza os valores para a próxima repetição
        anterior = atual
        atual = proximo

        # Incrementa o contador para controlar o while
        contador += 1

    # Executado uma única vez, após o término da sequência
    print('FIM')
