# # Exercício 62 - Progressão Aritmética (Parte 2)
# Versão 1: apresentação inicial e termos adicionais em laços separados.

# Entrada de dados
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Inicialização das variáveis de controle
termo = primeiro_termo
contador = 1
limite = 10

# Apresenta os dez primeiros termos da PA
while contador <= limite:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print()

# Solicita a quantidade de termos adicionais
mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

# Repete enquanto o usuário solicitar novos termos
while mais_termos != 0:
    limite += mais_termos

    # Continua a sequência sem reiniciar o contador
    while contador <= limite:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1

    print()
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))

# Mensagem de encerramento
print('FIM')

        

        
    
