'''Desenvolva um programa que leia:

o nome do produto
o preço unitário
a quantidade comprada
se o cliente é cadastrado na loja (S ou N)

Calcule o subtotal (preço unitário × quantidade).

Desconto por faixa de valor (sobre o subtotal):

Subtotal de até R$ 100,00 (inclusive): sem desconto
Subtotal acima de R$ 100,00 até R$ 500,00 (inclusive): 5% de desconto
Subtotal acima de R$ 500,00: 10% de desconto

Desconto de cliente cadastrado: se o cliente for cadastrado, ganha mais 3%, aplicado sobre o valor que já recebeu o desconto da faixa (e não sobre o subtotal original).

Ao final, exiba um relatório com: nome do produto, quantidade, subtotal, percentual de desconto da faixa, se houve desconto de cadastrado, total a pagar e quanto o cliente economizou (subtotal menos total a pagar).'''

# Calculadora de Desconto
nome_produto = input('Digite o nome do Produto: ')
preco_unitario = float(input('Digite o preço unitário do produto: '))
quantidade = int(input('Digite a quantidade comprada: '))
cliente_cadastrado = input('O cliente é cadastrado na loja? [S/N]: ').strip().upper()

Subtotal = preco_unitario * quantidade

if Subtotal <= 100:
    desconto_faixa = 0
elif Subtotal <= 500:
    desconto_faixa = 5
else:
    desconto_faixa = 10

desconto_cadastrado = 0 
if cliente_cadastrado == 'S':
    desconto_cadastrado = 3

valor_com_desconto_faixa = Subtotal * (1 - desconto_faixa / 100)
total_a_pagar = valor_com_desconto_faixa * (1 - desconto_cadastrado / 100)
economizado = Subtotal - total_a_pagar

print(f'Produto: {nome_produto}')
print(f'Quantidade:{quantidade}')
print(f'Subtotal: R${Subtotal:.2f}')
print(f'Desconto da faixa: {desconto_faixa}%')
print(f'Desconto de cliente cadastrado: {desconto_cadastrado}%')
print(f'Total a pagar: R${total_a_pagar:.2f}')
print(f'Você economizou: R${economizado:.2f}')
