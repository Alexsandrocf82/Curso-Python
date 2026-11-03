
# Exercício 62 - Progressão Aritmética (Parte 2)
# Versão 2: refatoração para evitar duplicação de código.

# Entrada de dados
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Inicialização das variáveis de controle
termo = primeiro_termo
contador = 1
total = 0
mais_termos = 10

# Controla a apresentação inicial e as solicitações adicionais
while mais_termos != 0:
    total += mais_termos

    # Apresenta apenas os termos ainda não exibidos
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1

    print()
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

# Exibe a quantidade total de termos apresentados
print(f'Progressão finalizada com {total} termos mostrados.')


