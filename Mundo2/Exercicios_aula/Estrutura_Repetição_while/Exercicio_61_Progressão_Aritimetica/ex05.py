# Exercício 61 — Progressão Aritmética (PA)
# Exibe os 10 primeiros termos de uma PA utilizando while.

# Entrada de dados
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Inicialização das variáveis
termo = primeiro_termo
contador = 1

# Cálculo e exibição dos 10 termos
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('FIM')
