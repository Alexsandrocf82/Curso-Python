# Exercício 60 — Fatorial (Versão 2)
# Calcula o fatorial utilizando while, com validação de números negativos.

# Entrada de dados
numero = int(input('Digite um número inteiro para calcular o seu fatorial: '))

# Validação de números negativos
if numero < 0:
    print('Erro! Fatorial não existe para números negativos. ')
else:
    # Inicialização das variáveis
    contador = numero
    fatorial = 1

    # Cálculo do fatorial
    while contador > 0:
        fatorial *= contador
        contador -= 1

    # Resultado final
    print(f'O fatorial de {numero} é {fatorial}')