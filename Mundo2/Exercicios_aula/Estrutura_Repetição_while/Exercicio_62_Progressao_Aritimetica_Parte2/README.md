# Exercício 62 — Progressão Aritmética (Parte 2)

## Objetivo

Desenvolver um programa em Python que apresente os dez primeiros termos de uma Progressão Aritmética (PA) e permita ao usuário solicitar quantos termos adicionais desejar. O programa deve encerrar quando o usuário informar `0`.

**Curso:** Python 3 — Mundo 2, Curso em Vídeo  
**Conteúdo:** Estruturas de repetição com `while`

## Versões desenvolvidas

### Versão 1 — `ex06.py`

Primeira implementação do exercício, utilizando um laço `while` para apresentar os dez primeiros termos e laços adicionais para controlar as novas solicitações.

**Características:**
- Apresentação dos dez primeiros termos.
- Solicitação de termos adicionais.
- Continuidade da sequência sem reiniciar o contador.
- Encerramento quando o usuário digita `0`.

### Versão 2 — `ex06_v2.py`

Refatoração da primeira solução para reduzir a duplicação de código.

**Melhorias:**
- Utilização de um único laço interno para apresentar os termos.
- Controle acumulativo da quantidade de termos com a variável `total`.
- Exibição da quantidade total de termos apresentados.
- Organização mais enxuta da estrutura de repetição.

## Exemplo de execução

```text
Digite o primeiro termo da PA: 3
Digite a razão da PA: 4
3 -> 7 -> 11 -> 15 -> 19 -> 23 -> 27 -> 31 -> 35 -> 39 ->
Quantos termos você quer mostrar a mais? 5
43 -> 47 -> 51 -> 55 -> 59 ->
Quantos termos você quer mostrar a mais? 3
63 -> 67 -> 71 ->
Quantos termos você quer mostrar a mais? 0
Progressão finalizada com 18 termos mostrados.
```

*Exemplo correspondente à versão 2.*

## Conceitos praticados

- Estruturas de repetição `while`.
- Laços de repetição aninhados.
- Variáveis de controle e acumuladores.
- Condições de encerramento.
- Indentação em Python.
- Refatoração para reduzir duplicação de código.

## Aprendizados

O desenvolvimento das duas versões permitiu compreender como diferentes estruturas podem resolver o mesmo problema.

A primeira versão facilitou a construção gradual da lógica. A segunda demonstrou como reorganizar o programa para reutilizar instruções e melhorar a manutenção do código.

## Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git e GitHub
