# Exercício 60 — Fatorial (Versão 1)
# Calcula o fatorial de um número utilizando while.

# Entrada de dados
numero = int(input('Digite um número inteiro não negativo: '))

# Inicialização das variáveis
fatorial = 1
contador = numero

# Cálculo do fatorial
while contador > 0:
    fatorial *= contador
    contador -= 1
    print(fatorial)

# Resultado final
print(f'O fatorial de {numero} é {fatorial}')