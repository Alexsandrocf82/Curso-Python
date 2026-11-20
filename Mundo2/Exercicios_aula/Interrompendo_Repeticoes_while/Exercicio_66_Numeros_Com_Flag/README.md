
# Exercício 066 — Vários Números com Flag

## 1. Sobre o exercício

Exercício desenvolvido durante o curso Python 3 — Mundo 2,
ministrado pelo professor Gustavo Guanabara, do Curso em Vídeo.

O exercício integra a Aula 15 — Interrompendo Repetições while
e tem como finalidade consolidar a utilização do comando break,
de valores sentinelas, contadores e acumuladores.

## 2. Enunciado

Desenvolver um programa que leia vários números inteiros
pelo teclado e interrompa a execução quando o usuário
informar o valor 999.

Ao final, apresentar a quantidade de números informados
e a soma dos valores, desconsiderando o sentinela.

## 3. Objetivos de aprendizagem

- Compreender o funcionamento da estrutura while True.
- Utilizar o comando break para interromper repetições.
- Implementar um valor sentinela para controlar a execução.
- Trabalhar com contadores e acumuladores.
- Separar as responsabilidades das variáveis.
- Identificar e corrigir erros de lógica de programação.
- Validar algoritmos por meio de testes funcionais.

## 4. Funcionalidades

- Leitura contínua de números inteiros.
- Encerramento da repetição ao informar 999.
- Contabilização dos números válidos.
- Cálculo da soma dos valores informados.
- Exclusão do sentinela dos resultados.
- Apresentação de um relatório final.

As funcionalidades descritas correspondem à versão 2.0.

## 5. Conceitos aplicados

| Conceito | Aplicação |
|---|---|
| while True | Repetição contínua |
| if | Verificação da condição de encerramento |
| break | Interrupção do laço |
| Flag | Utilização de 999 como sentinela |
| Contador | Quantidade de números informados |
| Acumulador | Soma dos valores válidos |
| int() | Conversão da entrada para inteiro |
| f-strings | Formatação dos resultados |

## 6. Evolução do desenvolvimento

O exercício possui duas versões, representando o processo
de aprendizagem, identificação de erros e correção do algoritmo.

### Versão 1.0 — Implementação inicial

Arquivo: `ex01_v1.py`

A primeira implementação utilizava a variável `numero`
simultaneamente para armazenar o valor informado pelo
usuário e contabilizar as entradas.

A instrução:

```python
numero += 1
```

modificava indevidamente o valor informado antes de
adicioná-lo ao acumulador.

Além disso, após o encerramento da repetição, a variável
numero armazenava o sentinela 999, em vez da quantidade
de números válidos.

#### Exemplo da falha lógica

Entrada: 5, 8, 12, 999.

| Indicador | Resultado da V1 | Resultado esperado |
|---|---:|---:|
| Quantidade | 999 | 3 |
| Soma | 28 | 25 |

A V1 foi reconstruída com base nos registros do acompanhamento
dos estudos, preservando o erro lógico identificado.
O texto literal das mensagens originais não foi confirmado.

Essa versão possui finalidade histórica e educacional.

### Versão 2.0 — Correção e validação funcional

Arquivo: `ex01_v2.py`

Na segunda versão, foi criada uma variável exclusiva
para contabilizar os números informados:

```python
numeros_digitados = 0
```

A contagem e a soma passaram a utilizar instruções
independentes:

```python
numeros_digitados += 1
soma += numero
```

Essa alteração corrigiu os problemas identificados na
primeira implementação e garantiu a precisão dos resultados.

A correção foi desenvolvida autonomamente e validada
por meio de quatro testes funcionais.

## 7. Comparação entre as versões

| Critério | V1 | V2 |
|---|---|---|
| Estrutura while True | Correta | Correta |
| Utilização do break | Correta | Correta |
| Controle do sentinela | Correto | Correto |
| Contador | Incorreto | Correto |
| Acumulador | Incorreto | Correto |
| Responsabilidade das variáveis | Inadequada | Adequada |
| Resultado funcional | Incorreto | Aprovado |

## 8. Estrutura do exercício

```text
Exercicio_66_Numeros_Com_Flag/
├── ex01_v1.py
├── ex01_v2.py
└── README.md
```

| Arquivo | Descrição |
|---|---|
| ex01_v1.py | Reconstrução da implementação inicial com erro lógico |
| ex01_v2.py | Implementação corrigida e validada |
| README.md | Documentação técnica do exercício |

## 9. Como executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento Python.

Acesse a pasta do exercício e execute a versão desejada.

### Versão 1.0 — Análise do erro

```bash
python ex01_v1.py
```

### Versão 2.0 — Versão recomendada

```bash
python ex01_v2.py
```

Informe os números inteiros solicitados pelo programa.
Digite 999 para encerrar a execução.

## 10. Testes funcionais

Testes realizados em 18/11/2026, utilizando a versão 2.0.

| Teste | Entradas | Quantidade | Soma | Situação |
|---|---|---:|---:|---|
| 01 | 5, 8, 12, 999 | 3 | 25 | Aprovado |
| 02 | 999 | 0 | 0 | Aprovado |
| 03 | 10, -5, 0, 15, 999 | 4 | 20 | Aprovado |
| 04 | 998, 1000, 999 | 2 | 1998 | Aprovado |

Resultado: 4 de 4 testes aprovados.

Aproveitamento: 100%.

## 11. Avaliação técnica

- Versão avaliada: 2.0.
- Nota: 10,0/10.
- Data de validação: 18/11/2026.
- Situação: implementação final validada.

A versão 2.0 atende aos requisitos funcionais do
enunciado original.

## 12. Limitações e possibilidades de evolução

O programa pressupõe que o usuário informe números inteiros.

A implementação não possui tratamento de exceções para
entradas não numéricas.

Como possibilidade de evolução futura, poderá ser
implementado o tratamento de entradas inválidas utilizando
estruturas de exceção.

## 13. Aprendizados consolidados

O desenvolvimento deste exercício permitiu compreender
a importância da separação das responsabilidades das
variáveis dentro de um algoritmo.

Também contribuiu para desenvolver competências relacionadas
à análise de erros, depuração lógica, elaboração de testes
e correção autônoma de programas.

## 14. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop
- Markdown

## 15. Referências

- [Curso em Vídeo](https://www.cursoemvideo.com/)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [PEP 257](https://peps.python.org/pep-0257/)

## 16. Autor

**Alexsandro Ferreira**

Estudante de Engenharia de Software e Professor.

Projeto desenvolvido como parte do processo de formação
em programação e desenvolvimento de software.

[Meu GitHub](https://github.com/Alexsandrocf82)
