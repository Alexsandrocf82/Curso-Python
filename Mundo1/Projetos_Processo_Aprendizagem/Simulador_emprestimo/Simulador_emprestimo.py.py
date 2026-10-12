'''Desenvolva um programa que leia:

o nome do cliente
o valor do empréstimo solicitado
o número de parcelas
a renda mensal do cliente

Regras de prazo (portão de entrada): o prazo mínimo é de 1 parcela e o máximo de 48 parcelas. Se o número de parcelas estiver fora desse intervalo, o programa mostra uma mensagem de prazo inválido e não calcula mais nada.

Taxa de juros mensal (juros simples), conforme o prazo:

De 1 a 12 parcelas (inclusive): 2% ao mês
De 13 a 24 parcelas (inclusive): 3% ao mês
De 25 a 48 parcelas (inclusive): 4% ao mês

Cálculos:

Total de juros = valor solicitado × taxa mensal × número de parcelas
Total a pagar = valor solicitado + total de juros
Valor da parcela = total a pagar ÷ número de parcelas

Regra de aprovação: o empréstimo é aprovado se o valor da parcela comprometer até 30% da renda mensal (inclusive). Acima disso, é negado.

Ao final, exiba um relatório com: nome do cliente, valor solicitado, número de parcelas, taxa de juros aplicada, total a pagar, valor da parcela, percentual da renda comprometido pela parcela e o resultado (Aprovado ou Negado).'''

# Entrada de dados 
nome_cliente = input('Digite o nome do cliente: ')
valor_emprestimo = float(input('Digite o valor do empréstimo solicitado: '))
numero_parcelas = int(input('Digite o número de parcelas: '))
renda_mensal = float(input('Digite a renda mensal do cliente: '))

# Validação do Prazo
if numero_parcelas < 1 or numero_parcelas > 48:
    print('Prazo inválido. O número de parcelas deve estar entre 1 e 48. ')
else: 
    # Cálculo da taxa de juros
    if numero_parcelas <= 12:
        taxa_juros = 2
    elif numero_parcelas <= 24:
        taxa_juros = 3
    else:
        taxa_juros = 4

    # Cálculo do total de juros, total a pagar e valor da parcela
    total_juros = valor_emprestimo * taxa_juros / 100 * numero_parcelas
    total_a_pagar = valor_emprestimo + total_juros
    valor_parcela = total_a_pagar / numero_parcelas

    # Cálculo do percentual da renda comprometido pela parcela
    percentual_renda = (valor_parcela / renda_mensal) * 100

    # Verificação de aprovação do empréstimo
    if percentual_renda <= 30:
        resultado = 'Aprovado'
    else:
        resultado = 'Negado'

    # Relatório final
    print(f'Nome do cliente: {nome_cliente}')
    print(f'Valor solicitado: R${valor_emprestimo:.2f}')
    print(f'Número de parcelas: {numero_parcelas}')
    print(f'Taxa de juros aplicada: {taxa_juros}%')
    print(f'Total a pagar: R${total_a_pagar:.2f}')
    print(f'Valor da Parcela: R${valor_parcela:.2f}')
    print(f'Percentual da renda comprometido pela parcela:  {percentual_renda:.2f}%')
    print(f'Resultado: {resultado}')


