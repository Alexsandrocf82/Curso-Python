
# ==========================================================
# PROJETO AUTORAL 09 - SISTEMA DE CONTROLE DE VENDAS E ESTOQUE
# Empresa: Cube Store SLZ
# Versão: 1.0
# Linguagem: Python
# ==========================================================

# Objetivo:
# Desenvolver um sistema básico de controle de estoque e vendas,
# permitindo consultar produtos, registrar vendas, validar
# quantidades e apresentar um relatório final das operações.


# ==========================================================
# 1. INICIALIZAÇÃO DAS VARIÁVEIS
# ==========================================================

produto = 'RS3M V5 MagLev'
estoque = 20

# Acumulador responsável por armazenar o total de unidades vendidas
vendas_quantidade = 0

# Variável responsável pelo controle do menu principal
opcao = 0


# ==========================================================
# 2. ESTRUTURA DE REPETIÇÃO E MENU PRINCIPAL
# ==========================================================

# Mantém o sistema em execução até que o usuário selecione a opção 3
while opcao != 3:
    print('===== CUBE STORE SLZ =====')
    print('[1] Consultar estoque')
    print('[2] Registrar Venda')
    print('[3] Encerrar sistema')

    # Recebe a opção escolhida pelo usuário
    opcao = int(input('Digite uma opção: '))

    # ======================================================
    # 3. CONSULTA DE ESTOQUE
    # ======================================================

    if opcao == 1:
        print('Consulta de estoque selecionada.')
        print(f'Produto: {produto}')
        print(f'Quantidade em Estoque: {estoque}')

    # ======================================================
    # 4. REGISTRO DE VENDAS
    # ======================================================

    elif opcao == 2:
        print('Registro de venda selecionado.')
        print(f'Produto: {produto}')
        print(f'Quantidade em Estoque: {estoque}')

        # Recebe a quantidade de unidades que serão vendidas
        quantidade_vendida = int(input('Digite a quantidade vendida: '))

        # ==================================================
        # 5. VALIDAÇÃO DA QUANTIDADE E DO ESTOQUE
        # ==================================================

        # Impede o registro de quantidades iguais a zero ou negativas
        if quantidade_vendida > 0:

            # Verifica se existe estoque suficiente para realizar a venda
            if quantidade_vendida <= estoque:

                # Atualiza o estoque após uma venda válida
                estoque -= quantidade_vendida

                # Acumula a quantidade total de unidades vendidas
                vendas_quantidade += quantidade_vendida

                # Apresenta a confirmação da venda e o estoque atualizado
                print('Venda realizada com sucesso!')
                print(f'Quantidade vendida: {quantidade_vendida}')
                print(f'Quantidade em Estoque: {estoque}')

            else:
                # Impede vendas superiores ao estoque disponível
                print('Quantidade em estoque Insuficiente')

        else:
            # Informa que a quantidade digitada não é válida
            print('Quantidade Inválida!')

    # ======================================================
    # 6. RELATÓRIO FINAL E ENCERRAMENTO DO SISTEMA
    # ======================================================

    elif opcao == 3:

        # Apresenta o resumo das operações realizadas durante a execução
        print('===== Relatório de Vendas =====')
        print(f'Produto: {produto}')
        print(f'Quantidade em Estoque: {estoque}')
        print(f'Quantidade vendida: {vendas_quantidade}')
        print('Encerrar sistema!')

    # ======================================================
    # 7. TRATAMENTO DE OPÇÕES INVÁLIDAS DO MENU
    # ======================================================

    else:
        print('Opção inválida!')
