
# Exercício 63 - Sequência de Fibonacci
# Versão 1: solução inicial utilizando a estrutura de repetição while.

# Entrada de dados
quantidade = int(input('Digite a quantidade de termos que deseja mostrar: '))

# Inicialização das variáveis
anterior = 0
atual = 1
contador = 1

# Apresenta a quantidade de termos solicitada
while contador <= quantidade:
    # Exibe o termo atual da sequência
    print(anterior, end=' -> ')

    # Calcula o próximo termo somando os dois anteriores
    proximo = anterior + atual

    # Atualiza os valores para a próxima repetição
    anterior = atual
    atual = proximo

    # Incrementa o contador
    contador += 1

# Mensagem de encerramento
print('FIM')
