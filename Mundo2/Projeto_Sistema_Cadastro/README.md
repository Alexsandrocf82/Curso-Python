# Projeto 07 — Sistema de Cadastro em Python

## Sobre o projeto

O Sistema de Cadastro é um projeto desenvolvido em Python com o objetivo de aplicar e consolidar conhecimentos de lógica de programação, estruturas condicionais, estruturas de repetição e validação de dados.

O projeto foi construído em três versões progressivas, demonstrando a evolução das funcionalidades e a aplicação de novos conceitos durante o processo de aprendizagem.

## Tecnologias utilizadas

- Python 3
- VS Code
- Git e GitHub

## Evolução do projeto

### Versão 1 — Cadastro com estruturas condicionais

Implementação inicial de um sistema de cadastro individual.

**Funcionalidades:**
- Cadastro de nome, idade e sexo.
- Validação básica dos dados informados.
- Classificação automática por faixa etária.
- Exibição das informações cadastradas.

**Conceitos aplicados:** variáveis, operadores lógicos e estruturas condicionais (`if`, `elif` e `else`).

### Versão 2 — Cadastro com estruturas de repetição

Ampliação do sistema para permitir múltiplos cadastros e gerar estatísticas gerais.

**Funcionalidades:**
- Cadastro de várias pessoas.
- Validação contínua das entradas com `while`.
- Contagem total de pessoas cadastradas.
- Contagem de homens e mulheres.
- Cálculo da média de idade.
- Controle de continuidade dos cadastros.
- Verificação preventiva para evitar divisão por zero no cálculo da média.

**Conceitos aplicados:** estruturas de repetição, contadores, acumuladores, operadores lógicos e programação defensiva.

### Versão 3 — Cadastro com estatísticas por faixa etária

Evolução da Versão 2, acrescentando a distribuição das pessoas cadastradas por faixa etária.

**Funcionalidades:**
- Todas as funcionalidades da Versão 2.
- Contagem de crianças, adolescentes, adultos e idosos.
- Relatório estatístico consolidado.
- Validação das respostas de continuidade.
- Proteção preventiva contra divisão por zero.

**Conceitos aplicados:** estruturas condicionais e de repetição, validação de dados, contadores, acumuladores, cálculo de médias e programação defensiva.

## Regras de validação

O sistema utiliza as seguintes regras:

| Campo | Regra |
|---|---|
| Nome | Não pode estar vazio ou conter apenas espaços |
| Idade | Número inteiro entre 0 e 120 anos |
| Sexo | Aceita M ou F, desconsiderando diferenças entre maiúsculas e minúsculas e espaços nas extremidades |
| Continuidade | Aceita somente S ou N nas versões com múltiplos cadastros |

### Classificação por faixa etária

| Faixa etária | Idade |
|---|---|
| Criança | 0 a 11 anos |
| Adolescente | 12 a 17 anos |
| Adulto | 18 a 59 anos |
| Idoso | 60 a 120 anos |

## Organização dos arquivos

```text
Projeto_07_Sistema_Cadastro/
├── cadastro_v1_condicionais.py
├── cadastro_v2_repeticao.py
├── cadastro_v3_estatisticas.py
└── README.md
```

## Como executar

1. Instale o Python 3 no computador.
2. Abra a pasta do projeto no VS Code ou em um terminal.
3. Execute a versão desejada.

Para executar a versão mais completa:

```bash
python cadastro_v3_estatisticas.py
```

4. Informe os dados solicitados e acompanhe os resultados apresentados no terminal.

## Testes realizados

A Versão 3 foi submetida a sete cenários de testes manuais:

1. Cadastro individual com dados válidos.
2. Validação de nomes vazios ou contendo apenas espaços.
3. Validação de idades inválidas.
4. Validação das entradas de sexo.
5. Verificação dos limites das faixas etárias.
6. Realização de múltiplos cadastros e conferência das estatísticas.
7. Validação das respostas de continuidade.

Os sete cenários foram concluídos com os resultados esperados.

## Aprendizados

O desenvolvimento deste projeto permitiu compreender a utilização de estruturas condicionais e de repetição na resolução de problemas, a importância da validação de dados e a aplicação de contadores e acumuladores para produzir informações estatísticas.

Também contribuiu para a compreensão da programação defensiva, especialmente na prevenção de erros durante o cálculo da média de idade.

## Desenvolvimento

Projeto desenvolvido como parte dos estudos de Python, com apoio de ferramentas de inteligência artificial para orientação, revisão e análise de testes.

A organização em três versões permite acompanhar a evolução da solução e dos conhecimentos aplicados.