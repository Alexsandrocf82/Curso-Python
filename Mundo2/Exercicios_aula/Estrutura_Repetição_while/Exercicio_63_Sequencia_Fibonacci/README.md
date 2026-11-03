
# Exercício 63 — Sequência de Fibonacci

## Descrição

Programa desenvolvido em Python como parte dos estudos
do Curso em Vídeo — Python 3, Mundo 2.

O objetivo do exercício é solicitar ao usuário uma quantidade
de termos e apresentar os primeiros números da Sequência
de Fibonacci utilizando a estrutura de repetição `while`.

Na Sequência de Fibonacci, cada termo, a partir do terceiro,
é obtido pela soma dos dois anteriores.

Exemplo:
0 → 1 → 1 → 2 → 3 → 5 → 8 → 13

## Versão 1 — ex63.py

Primeira solução desenvolvida utilizando:

- Entrada de dados com `input()`.
- Conversão de dados com `int()`.
- Estrutura de repetição `while`.
- Variáveis para armazenar os termos da sequência.
- Contador para controlar as repetições.

Esta versão não possui validação para quantidades
menores ou iguais a zero.

## Versão 2 — ex63_v2.py

A segunda versão mantém a lógica original e acrescenta:

- Validação de quantidades não positivas.
- Estrutura condicional `if/else`.
- Mensagem para quantidade inválida.
- Encerramento somente após uma sequência válida.

## Exemplo de execução

Entrada:
Digite a quantidade de termos: 8

Saída:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> FIM

## Testes realizados

- 8 termos: sequência correta.
- 3 termos: sequência correta.
- 1 termo: sequência correta.
- 0 termos: mensagem de quantidade inválida.
- -3 termos: mensagem de quantidade inválida.
- 8 termos após a validação: sequência correta.

Os três primeiros testes foram realizados na versão inicial.
Os demais foram realizados na versão melhorada.

## Conceitos praticados

- Estruturas de repetição com `while`.
- Estruturas condicionais com `if/else`.
- Atualização de variáveis.
- Contadores.
- Indentação.
- Validação de entrada numérica.
- Testes funcionais.

## Observação

A versão 2 valida quantidades inteiras menores ou iguais
a zero. Entradas não numéricas ainda não são tratadas.

## Evolução do exercício

O desenvolvimento foi dividido em duas etapas:

1. Construção da sequência utilizando `while`.
2. Melhoria do programa com validação de quantidade.

Essa organização permite acompanhar a evolução da
solução e os conceitos aprendidos.
