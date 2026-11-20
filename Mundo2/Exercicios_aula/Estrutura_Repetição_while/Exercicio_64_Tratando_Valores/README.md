
# Exercício 064 — Tratando Vários Valores

## Sobre o exercício

Exercício desenvolvido durante o curso Python 3 — Mundo 2,
do Curso em Vídeo, ministrado pelo professor Gustavo Guanabara.

## Objetivo

Desenvolver um programa que leia vários números inteiros
pelo teclado, encerrando a execução quando o usuário
informar o valor 999.

Ao final, o programa apresenta a quantidade de números
digitados e a soma dos valores, desconsiderando o valor
sentinela.

## Funcionalidades

- Leitura de números inteiros.
- Contagem dos valores informados.
- Soma dos números digitados.
- Encerramento por meio do valor sentinela 999.
- Apresentação dos resultados ao usuário.

## Conceitos aplicados

- Estrutura de repetição while.
- Operadores relacionais.
- Contadores e acumuladores.
- Valor sentinela.
- Entrada e saída de dados.
- Formatação de strings com f-strings.

## Estrutura do projeto

- ex064.py — Código-fonte do exercício.
- README.md — Documentação do exercício.

## Como executar

```bash
python ex064.py
```

## Testes funcionais

| Entradas | Quantidade | Soma | Resultado |
|---|---:|---:|---|
| 5, 10, 15, 999 | 3 | 30 | Aprovado |
| 999 | 0 | 0 | Aprovado |
| 10, -5, 0, 15, 999 | 4 | 20 | Aprovado |
| 998, 1000, 999 | 2 | 1998 | Aprovado |

## Avaliação técnica

- Nota: 10,0/10.
- Testes funcionais: 4 de 4 aprovados.
- Validação final: 20/11/2026.

## Limitações

O programa pressupõe que o usuário informe números
inteiros válidos. O tratamento de entradas não numéricas
não faz parte do escopo desta versão.

## Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

## Autor

Alexsandro Ferreira

Estudante de Engenharia de Software.

Projeto desenvolvido para fins de aprendizagem e
consolidação dos fundamentos da programação.
