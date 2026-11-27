
# 📦 Projeto Autoral 09 — Sistema de Controle de Vendas e Estoque

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Versão](https://img.shields.io/badge/Versão-1.0-blue)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Testes](https://img.shields.io/badge/Testes-10%2F10-brightgreen)

## 📋 Sobre o Projeto

O Sistema de Controle de Vendas e Estoque é um projeto autoral desenvolvido em Python, inspirado nas necessidades reais da Cube Store SLZ, loja especializada na comercialização de cubos mágicos.

O projeto tem como finalidade aplicar conhecimentos de lógica de programação e desenvolvimento de software na construção de uma solução para o gerenciamento de estoque e o registro de vendas.

Seu desenvolvimento segue uma abordagem incremental, na qual novas funcionalidades serão incorporadas conforme a evolução dos conhecimentos em programação.

## 🎯 Objetivos

- Aplicar conceitos de programação na resolução de problemas reais.
- Desenvolver um sistema interativo utilizando o terminal.
- Consultar a quantidade de produtos disponíveis em estoque.
- Registrar vendas e atualizar automaticamente o estoque.
- Implementar regras de negócio e validação de dados.
- Gerar relatórios consolidados das operações realizadas.
- Desenvolver competências relacionadas à Engenharia de Software.

## ⚙️ Funcionalidades da V1

- Menu principal interativo.
- Consulta do produto disponível.
- Consulta da quantidade em estoque.
- Registro de vendas.
- Validação de quantidades positivas.
- Verificação de disponibilidade em estoque.
- Bloqueio de vendas superiores ao estoque disponível.
- Bloqueio de vendas com estoque zerado.
- Atualização automática do estoque.
- Acumulação da quantidade total de unidades vendidas.
- Tratamento de opções inteiras inválidas no menu.
- Relatório final de vendas.
- Encerramento controlado do sistema.

## 📐 Regras de Negócio

| Regra | Descrição |
|---|---|
| RN01 | A quantidade vendida deve ser maior que zero. |
| RN02 | A quantidade vendida não pode ultrapassar o estoque disponível. |
| RN03 | Somente vendas válidas podem alterar o estoque. |
| RN04 | O estoque não pode apresentar valores negativos. |
| RN05 | Somente vendas válidas devem atualizar o acumulador de vendas. |
| RN06 | O sistema deve permanecer em execução até a opção de encerramento. |
| RN07 | O relatório final deve apresentar o estoque restante e o total de unidades vendidas. |

## 🛠️ Tecnologias Utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop

## 🧠 Conceitos de Programação Aplicados

- Variáveis e tipos de dados.
- Entrada e saída de dados.
- Conversão de tipos com `int()`.
- Formatação de strings com f-strings.
- Estruturas de repetição `while`.
- Estruturas condicionais `if`, `elif` e `else`.
- Estruturas condicionais aninhadas.
- Operadores relacionais.
- Operadores de atribuição composta (`+=` e `-=`).
- Acumuladores.
- Validação de regras de negócio.
- Testes funcionais.
- Documentação de código.
- Controle de versionamento.

## 📂 Estrutura do Projeto

```text
Projeto_09_Sistema_Vendas_Estoque/
│
├── estoque_v1.py
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento compatível.

### Execução

Acesse o diretório do projeto pelo terminal e execute:

```bash
python estoque_v1.py
```

Em sistemas Linux, caso necessário, utilize:

```bash
python3 estoque_v1.py
```

O sistema não necessita da instalação de bibliotecas externas.

## 💻 Demonstração de Funcionamento

### Menu principal

```text
===== CUBE STORE SLZ =====
[1] Consultar estoque
[2] Registrar Venda
[3] Encerrar sistema
Digite uma opção:
```

### Consulta de estoque

```text
Digite uma opção: 1

Consulta de estoque selecionada.
Produto: RS3M V5 MagLev
Quantidade em Estoque: 20
```

### Registro de venda

```text
Digite uma opção: 2

Registro de venda selecionado.
Produto: RS3M V5 MagLev
Quantidade em Estoque: 20

Digite a quantidade vendida: 3

Venda realizada com sucesso!
Quantidade vendida: 3
Quantidade em Estoque: 17
```

### Tentativa de venda com estoque insuficiente

```text
Digite uma opção: 2

Registro de venda selecionado.
Produto: RS3M V5 MagLev
Quantidade em Estoque: 17

Digite a quantidade vendida: 25

Quantidade em estoque Insuficiente
```

### Relatório final

```text
Digite uma opção: 3

===== Relatório de Vendas =====
Produto: RS3M V5 MagLev
Quantidade em Estoque: 17
Quantidade vendida: 3
Encerrar sistema!
```

## 🧪 Testes Funcionais

Foram realizados dez testes funcionais manuais para verificar o comportamento do sistema em diferentes cenários de utilização.

| Nº | Cenário testado | Resultado |
|---|---|---|
| 01 | Consulta do estoque inicial | Aprovado |
| 02 | Registro de venda de 3 unidades | Aprovado |
| 03 | Registro de venda de 5 unidades | Aprovado |
| 04 | Venda superior ao estoque disponível | Aprovado |
| 05 | Tentativa de venda de quantidade zero | Aprovado |
| 06 | Tentativa de venda de quantidade negativa | Aprovado |
| 07 | Venda de todas as unidades disponíveis | Aprovado |
| 08 | Tentativa de venda com estoque zerado | Aprovado |
| 09 | Seleção de opção inválida no menu | Aprovado |
| 10 | Relatório final e encerramento | Aprovado |

### Resultado da Validação

- Total de cenários testados: 10
- Testes aprovados: 10
- Testes reprovados: 0
- Taxa de aprovação: 100%

Os testes confirmaram que as vendas inválidas não alteram o estoque nem o acumulador de vendas.

## 📊 Evolução do Projeto

### Versão 1.0 — Sistema Básico

Status: Desenvolvimento concluído.

- Gerenciamento de um único produto.
- Consulta de estoque.
- Registro de vendas.
- Validação de quantidades inteiras.
- Controle de estoque.
- Acumulador de vendas.
- Relatório final.
- Testes funcionais.

### Versão 2.0 — Controle Financeiro e Robustez

Status: Planejada.

- Implementação do preço unitário do produto.
- Cálculo do valor de cada venda.
- Acumulador de faturamento.
- Validação de entradas não numéricas.
- Aprimoramento da interface.
- Relatório financeiro consolidado.

### Versão 3.0 — Gerenciamento de Múltiplos Produtos

Status: Planejada.

- Cadastro de múltiplos produtos.
- Controle individual de estoque.
- Reposição de mercadorias.
- Utilização de listas e dicionários.
- Organização do código em funções.
- Relatórios consolidados de vendas e estoque.

## ⚠️ Limitações Conhecidas da V1

- O sistema gerencia apenas um produto.
- Entradas não numéricas podem gerar uma exceção `ValueError`.
- Não possui controle de preços ou faturamento.
- Não permite reposição de mercadorias.
- Os dados são armazenados temporariamente na memória.
- As informações são reinicializadas quando o programa é executado novamente.
- Não possui integração com banco de dados.
- A interação ocorre exclusivamente pelo terminal.

Essas limitações fazem parte do escopo inicial do projeto e serão consideradas nas próximas etapas de desenvolvimento.

## 📚 Aprendizados

O desenvolvimento deste projeto possibilitou consolidar conhecimentos de lógica de programação por meio da implementação de uma solução relacionada a um problema real.

Entre os principais aprendizados, destacam-se:

- Transformação de necessidades reais em requisitos de software.
- Planejamento e desenvolvimento incremental.
- Implementação de regras de negócio.
- Integração de estruturas condicionais e de repetição.
- Controle da consistência dos dados.
- Manipulação de variáveis e acumuladores.
- Identificação e correção de erros.
- Execução de testes funcionais.
- Documentação técnica de software.
- Desenvolvimento com autonomia.

## 🎓 Contexto Acadêmico

Este projeto integra minha jornada de formação em Engenharia de Software e meus estudos de programação em Python, com ênfase na aplicação prática dos conhecimentos adquiridos durante o curso Python 3 — Mundo 2, do Curso em Vídeo.

O objetivo é construir um portfólio progressivo de projetos autorais, demonstrando a evolução das minhas competências em desenvolvimento de software.

## 👨‍💻 Autor

**Alexsandro Ferreira**

- Estudante de Engenharia de Software.
- Professor de Geografia e Mundo Computacional.
- Estudante de desenvolvimento de software.

GitHub: [Alexsandrocf82](https://github.com/Alexsandrocf82)

---

Projeto desenvolvido para fins educacionais e aprimoramento profissional, inspirado nas necessidades reais da Cube Store SLZ.

**Projeto Autoral 09 | Python | Engenharia de Software | 2026**
