
# Exercício 065 — Maior e Menor Valores

## Informações do exercício

- **Curso:** Python 3 — Mundo 2
- **Plataforma:** Curso em Vídeo
- **Professor:** Gustavo Guanabara
- **Aula:** 14 — Estrutura de repetição while
- **Exercício:** 065
- **Autor:** Alexsandro Ferreira
- **Versão:** 1.0
- **Data de validação:** 20/11/2026
- **Status:** Concluído e validado

## 1. Enunciado original

Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.

## 2. Objetivo

Desenvolver um programa capaz de receber uma quantidade
indeterminada de números inteiros, utilizando a estrutura
de repetição while para controlar a entrada de dados e
realizar operações estatísticas sobre os valores informados.

O exercício tem como objetivo consolidar o conhecimento
sobre estruturas de repetição, contadores, acumuladores,
estruturas condicionais e manipulação de variáveis.

## 3. Funcionalidades

- Leitura de números inteiros pelo teclado.
- Controle de continuidade da execução por meio das opções S/N.
- Contagem dos números informados.
- Acumulação dos valores digitados.
- Cálculo da média aritmética.
- Identificação do maior número informado.
- Identificação do menor número informado.
- Apresentação da soma total dos valores.
- Exibição dos resultados ao final da execução.

## 4. Implementação complementar autoral

Além dos requisitos solicitados no enunciado original,
foi implementada a apresentação da soma total dos números
informados pelo usuário.

Essa funcionalidade foi desenvolvida desde a primeira
implementação do exercício, sem a necessidade de criar
uma versão posterior.

A implementação complementar demonstra iniciativa na
ampliação das funcionalidades solicitadas e na aplicação
dos conceitos de acumulação de valores.

## 5. Conceitos de programação aplicados

- Variáveis e tipos de dados.
- Entrada e saída de dados.
- Conversão de valores com int().
- Estrutura de repetição while.
- Estruturas condicionais if e else.
- Operadores aritméticos.
- Operadores relacionais.
- Contadores e acumuladores.
- Controle de fluxo.
- Cálculo de média aritmética.
- Manipulação de strings com strip() e upper().
- Formatação de saída com f-strings.
- Documentação interna do código-fonte.
- Testes funcionais.

## 6. Estratégia de implementação

O programa utiliza uma variável de controle inicializada
com o valor S, permitindo a execução da estrutura while.

A cada repetição, um número inteiro é solicitado ao usuário.
O contador é incrementado e o valor informado é acrescentado
ao acumulador.

O primeiro número digitado é utilizado como referência
inicial para as variáveis que armazenam o maior e o menor
valor.

A partir do segundo número, são realizadas comparações
para atualizar essas variáveis sempre que necessário.

Essa estratégia permite identificar corretamente o maior
e o menor valor, inclusive em conjuntos formados
exclusivamente por números negativos.

Ao final de cada repetição, o usuário informa se deseja
continuar.

Quando a estrutura de repetição é encerrada, o programa
calcula a média aritmética e apresenta os resultados.

## 7. Estrutura do exercício

    Exercicio_65_Maior_Menor/
    ├── ex09.py
    └── README.md

| Arquivo | Descrição |
|---|---|
| ex09.py | Código-fonte comentado do exercício |
| README.md | Documentação técnica do exercício |

## 8. Como executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento compatível.

Acesse a pasta do exercício pelo terminal e execute:

```bash
python ex09.py
```

Informe os números inteiros solicitados pelo programa.

Digite S para continuar informando valores ou N para
encerrar a execução e visualizar os resultados.

## 9. Testes funcionais

Foram realizados quatro cenários de testes para verificar
o comportamento do algoritmo em diferentes condições.

| Teste | Valores informados | Soma | Média | Maior | Menor | Resultado |
|---|---|---:|---:|---:|---:|---|
| 01 | 5, 10, 15 | 30 | 10,00 | 15 | 5 | Aprovado |
| 02 | 8 | 8 | 8,00 | 8 | 8 | Aprovado |
| 03 | -8, -3, -12, -5 | -28 | -7,00 | -3 | -12 | Aprovado |
| 04 | 0, 0, 0 | 0 | 0,00 | 0 | 0 | Aprovado |

### Resumo dos testes

- Total de testes realizados: 4.
- Testes aprovados: 4.
- Testes reprovados: 0.
- Aproveitamento: 100%.

Os resultados confirmaram o funcionamento correto do
algoritmo nos cenários avaliados, incluindo números
positivos, negativos, valores iguais e entrada única.

## 10. Avaliação técnica

| Indicador | Resultado |
|---|---|
| Atendimento ao enunciado | Completo |
| Lógica de programação | Correta |
| Estrutura de repetição | Correta |
| Cálculos matemáticos | Corretos |
| Implementação complementar | Concluída |
| Testes funcionais | 4/4 aprovados |
| Nota técnica | 9,9/10 |

O algoritmo apresentou funcionamento correto em todos
os cenários avaliados.

A pequena dedução na avaliação técnica está relacionada
a aspectos ortográficos nas mensagens de saída, sem
comprometer o funcionamento do programa.

## 11. Limitações e melhorias futuras

A implementação atende aos requisitos originais do
exercício e à funcionalidade complementar proposta.

Entretanto, algumas melhorias poderão ser realizadas
futuramente:

- Validação de entradas não numéricas.
- Tratamento de exceções.
- Validação específica das opções S/N.
- Aprimoramento da apresentação dos resultados.
- Padronização ortográfica das mensagens de saída.

Essas melhorias não fazem parte dos requisitos obrigatórios
do exercício original.

## 12. Histórico de versões

### Versão 1.0

- Implementação completa do enunciado original.
- Controle de repetição com while.
- Cálculo da média aritmética.
- Identificação do maior e do menor valor.
- Implementação complementar da soma total.
- Inclusão de comentários técnicos no código-fonte.
- Validação em quatro cenários de testes funcionais.
- Elaboração da documentação técnica.

O exercício foi disponibilizado em uma única versão,
preservando a autenticidade do processo de desenvolvimento.

## 13. Tecnologias e ferramentas utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop
- Markdown

## 14. Aprendizados adquiridos

A realização deste exercício contribuiu para o
desenvolvimento das seguintes competências:

- Controle de estruturas de repetição.
- Manipulação de contadores e acumuladores.
- Identificação de valores máximos e mínimos.
- Processamento de conjuntos de dados.
- Desenvolvimento de algoritmos estatísticos.
- Ampliação autônoma de funcionalidades.
- Validação de algoritmos por meio de testes funcionais.
- Documentação e versionamento de código-fonte.

## 15. Autor

**Alexsandro Ferreira**

Estudante de Engenharia de Software.

Projeto desenvolvido durante o processo de aprendizagem
da linguagem Python, como parte da formação em
programação e desenvolvimento de software.

---

Exercício desenvolvido com finalidade educacional,
integrando o portfólio de aprendizagem em Python.
