
# Exercício 067 — Tabuada v3.0

## 1. Sobre o exercício

Exercício desenvolvido durante o curso Python 3 — Mundo 2,
ministrado pelo professor Gustavo Guanabara, do Curso em Vídeo.

O exercício integra a Aula 15 — Interrompendo Repetições while
e aborda a utilização integrada das estruturas de repetição
while e for, associadas ao comando break.

## 2. Enunciado

Desenvolver um programa que apresente a tabuada de
multiplicação de vários números inteiros informados pelo
usuário, interrompendo a execução quando for digitado
um número negativo.

## 3. Objetivos de aprendizagem

- Consolidar a utilização da estrutura while True.
- Utilizar o comando break para encerrar repetições.
- Integrar as estruturas de repetição while e for.
- Compreender o funcionamento de laços aninhados.
- Utilizar a função range() para controlar iterações.
- Aplicar operadores relacionais e aritméticos.
- Organizar a apresentação dos resultados.
- Validar o comportamento do algoritmo.

## 4. Funcionalidades

- Leitura contínua de números inteiros.
- Geração automática da tabuada de multiplicação.
- Apresentação dos multiplicadores de 1 a 10.
- Geração de múltiplas tabuadas durante uma execução.
- Suporte ao cálculo da tabuada de zero.
- Encerramento ao informar qualquer número negativo.
- Exibição de mensagem de encerramento.

## 5. Conceitos aplicados

| Conceito | Aplicação |
|---|---|
| while True | Controle da repetição principal |
| for | Geração da tabuada |
| Laços aninhados | Integração das repetições |
| if | Verificação de números negativos |
| break | Encerramento do laço principal |
| range(1, 11) | Geração dos multiplicadores de 1 a 10 |
| Operador relacional | Verificação da condição numero < 0 |
| Operador aritmético | Cálculo da multiplicação |
| f-strings | Formatação e alinhamento da saída |

## 6. Estratégia de implementação

O algoritmo foi desenvolvido utilizando duas estruturas
de repetição com responsabilidades distintas.

### Estrutura externa — while

Responsável pela leitura contínua dos números informados
pelo usuário.

### Condição de encerramento

A condição:

```python
if numero < 0:
    break
```

interrompe o laço principal antes que a tabuada de um
número negativo seja gerada.

### Estrutura interna — for

A estrutura:

```python
for c in range(1, 11):
```

é responsável pela geração dos multiplicadores de 1 a 10.

Após concluir cada tabuada, o programa retorna ao início
do laço principal para receber um novo número.

## 7. Fluxo de execução

1. Iniciar a estrutura de repetição while.
2. Solicitar um número inteiro.
3. Verificar se o número é negativo.
4. Caso seja negativo, interromper a repetição.
5. Caso contrário, gerar a tabuada de 1 a 10.
6. Solicitar um novo número.
7. Apresentar a mensagem de encerramento após o break.

## 8. Estrutura do exercício

```text
Exercicio_67_Tabuada/
├── ex02.py
└── README.md
```

| Arquivo | Descrição |
|---|---|
| ex02.py | Código-fonte comentado do exercício |
| README.md | Documentação técnica do exercício |

## 9. Como executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento Python.

Acesse a pasta do exercício e execute:

```bash
python ex02.py
```

Informe um número inteiro para visualizar sua tabuada.

Para encerrar o programa, informe qualquer número negativo.

## 10. Exemplo de execução

```text
Digite um número inteiro: 5
5 x  1 = 5
5 x  2 = 10
5 x  3 = 15
5 x  4 = 20
5 x  5 = 25
5 x  6 = 30
5 x  7 = 35
5 x  8 = 40
5 x  9 = 45
5 x 10 = 50
Digite um número inteiro: -1
Programa encerrado
```

## 11. Testes funcionais

Testes realizados em 18/11/2026.

| Teste | Entradas | Resultado | Situação |
|---|---|---|---|
| 01 | 5, -1 | Tabuada de 5 com 10 operações | Aprovado |
| 02 | -3 | Encerramento sem gerar tabuada | Aprovado |
| 03 | 0, -1 | Dez produtos iguais a zero | Aprovado |
| 04 | 2, 7, 10, -5 | Três tabuadas e 30 operações | Aprovado |

Resultado: 4 de 4 testes aprovados.

Aproveitamento: 100%.

## 12. Avaliação técnica

- Versão avaliada: 1.0.
- Nota: 10,0/10.
- Data de validação: 18/11/2026.
- Situação: implementação final validada.

O algoritmo foi desenvolvido autonomamente e atendeu
aos requisitos funcionais do enunciado desde a primeira
implementação.

## 13. Versionamento

### Versão 1.0 — Implementação validada

Arquivo: `ex02.py`.

Esta versão contempla todas as funcionalidades exigidas
pelo exercício original.

Não houve necessidade de desenvolver uma segunda versão,
pois a implementação inicial foi aprovada nos testes
funcionais realizados.

A expressão Tabuada v3.0 corresponde ao título original
do exercício do Curso em Vídeo, e não ao número de versões
desenvolvidas pelo autor.

## 14. Limitações e possibilidades de evolução

O programa pressupõe que o usuário informe números inteiros.

Entradas não numéricas não possuem tratamento de exceções.

Possíveis evoluções futuras:

- Tratamento de entradas inválidas.
- Personalização do intervalo dos multiplicadores.
- Organização da apresentação em funções.
- Desenvolvimento de uma interface interativa.

Essas funcionalidades não integram o escopo da versão atual.

## 15. Aprendizados consolidados

O desenvolvimento deste exercício permitiu consolidar
a utilização integrada de estruturas de repetição.

A implementação reforçou a compreensão de laços aninhados,
condições de encerramento, controle de fluxo e utilização
do comando break.

Também contribuiu para o desenvolvimento da autonomia
na elaboração e validação de algoritmos.

## 16. Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop
- Markdown

## 17. Referências

- [Curso em Vídeo](https://www.cursoemvideo.com/)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [PEP 8](https://peps.python.org/pep-0008/)
- [PEP 257](https://peps.python.org/pep-0257/)

## 18. Autor

**Alexsandro Ferreira**

Estudante de Engenharia de Software e Professor.

Projeto desenvolvido como parte do processo de formação
em programação e desenvolvimento de software.

[Meu GitHub](https://github.com/Alexsandrocf82)
