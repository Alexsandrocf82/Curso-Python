'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos'''

frase = input('Digite uma frase: ')
frase = frase.replace(" ", "").lower()

frase_invertida = ""
for c in range(len(frase) -1, -1, -1):
    frase_invertida = frase_invertida + frase[c]
if frase == frase_invertida:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palíndromo')


    '''
Outra forma de resolver (solução do professor):
- usa .strip() para remover espaços do início/fim da frase
- usa .split() + ''.join() para remover espaços do meio, em vez de .replace()
- usa .upper() em vez de .lower() (funciona igual, só muda a direção da conversão)
- usa += como atalho para "frase_invertida = frase_invertida + junto[letra]"

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
'''

