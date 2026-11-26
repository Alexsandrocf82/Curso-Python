# Exercício 069 - Análise de Dados do Grupo

## Sobre o exercício

Este exercício faz parte do curso Python 3 - Mundo 2,
do Curso em Vídeo, ministrado pelo professor Gustavo Guanabara.

O programa realiza o cadastro de várias pessoas, coletando
informações sobre idade e sexo, processando os dados e
apresentando um relatório estatístico ao final da execução.

O exercício foi desenvolvido em duas versões, demonstrando
a evolução incremental do código, a validação de dados e
a melhoria da experiência do usuário.

---

## Objetivos

- Praticar estruturas de repetição.
- Utilizar estruturas condicionais independentes e aninhadas.
- Trabalhar com múltiplos contadores.
- Implementar mecanismos de validação de dados.
- Controlar o fluxo de execução com break e continue.
- Aprimorar a apresentação de programas no terminal.
- Desenvolver habilidades de debugging e testes funcionais.
- Praticar o versionamento de código com Git e GitHub.

---

## Enunciado

Crie um programa que leia a idade e o sexo de várias pessoas.

A cada pessoa cadastrada, o programa deverá perguntar
se o usuário deseja continuar.

Ao final, mostre:

- Quantas pessoas têm mais de 18 anos.
- Quantos homens foram cadastrados.
- Quantas mulheres têm menos de 20 anos.

---

## Funcionalidades

- Cadastro de múltiplas pessoas.
- Entrada de idade e sexo.
- Validação das opções de sexo.
- Validação da opção de continuidade.
- Contagem de pessoas com mais de 18 anos.
- Contagem de homens cadastrados.
- Contagem de mulheres com menos de 20 anos.
- Encerramento controlado pelo usuário.
- Apresentação de relatório estatístico final.

---

## Evolução das versões

### V1 - Implementação inicial

Arquivo: `ex04_v1.py`

A primeira versão implementa as funcionalidades
fundamentais solicitadas no enunciado.

Principais características:

- Utilização de while True.
- Inicialização e atualização de contadores.
- Estruturas condicionais independentes.
- Validação do sexo informado.
- Validação da opção de continuidade.
- Encerramento utilizando break.
- Apresentação dos resultados finais.

Limitações:

- Não possui validação numérica da idade.
- Entradas não numéricas podem gerar ValueError.
- Permite o cadastro de idades negativas.
- Apresentação visual simplificada.

### V2 - Validação de dados e melhoria da interface

Arquivo: `ex04_v2.py`

A segunda versão preserva as funcionalidades da V1
e acrescenta mecanismos de validação numérica e
melhorias na apresentação visual.

Principais melhorias:

- Recebimento inicial da idade como string.
- Validação numérica utilizando isdigit().
- Conversão para inteiro após a validação.
- Rejeição de letras, entradas vazias, números
  decimais e negativos nos formatos usuais.
- Utilização de continue para entradas inválidas.
- Cabeçalho principal do sistema.
- Identificação visual dos cadastros.
- Centralização de títulos utilizando center().
- Separadores horizontais.
- Relatório final formatado.
- Mensagem de encerramento do sistema.

---

## Comparativo entre as versões

| Funcionalidade | V1 | V2 |
|---|---|---|
| Cadastro de pessoas | Sim | Sim |
| Contagem por idade e sexo | Sim | Sim |
| Validação do sexo | Sim | Sim |
| Validação da continuidade | Sim | Sim |
| Controle com break | Sim | Sim |
| Validação numérica da idade | Não | Sim |
| Rejeição de idades negativas | Não | Sim |
| Tratamento de entradas vazias na idade | Não | Sim |
| Utilização de continue | Não | Sim |
| Cabeçalhos centralizados | Não | Sim |
| Separadores visuais | Não | Sim |
| Relatório formatado | Não | Sim |
| Mensagem de encerramento | Não | Sim |

---

## Conceitos de programação aplicados

### Estruturas de repetição

- while
- while True

### Estruturas condicionais

- if
- elif
- Condições independentes
- Condições aninhadas
- Operadores relacionais
- Operadores lógicos

### Controle de fluxo

- break
- continue

### Manipulação de strings

- strip()
- upper()
- isdigit()
- center()

### Outros conceitos

- Variáveis
- Contadores
- Operador de incremento +=
- Conversão de tipos com int()
- Entrada de dados com input()
- Saída de dados com print()
- Formatação com f-strings
- Validação de entradas
- Indentação
- Desenvolvimento incremental
- Testes funcionais
- Testes de regressão

---

## Tecnologias e ferramentas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop

O programa utiliza exclusivamente recursos nativos
da linguagem Python, sem dependências externas.

---

## Estrutura dos arquivos

```text
Exercicio_69_Analise_Dados_Grupo/
├── ex04_v1.py
├── ex04_v2.py
└── README.md
```

---

## Como executar

### Pré-requisitos

- Python 3 instalado.
- Terminal ou ambiente de desenvolvimento Python.

Acesse a pasta do exercício pelo terminal.

### Executar a versão V1

```bash
python ex04_v1.py
```

### Executar a versão V2

```bash
python ex04_v2.py
```

Em sistemas Linux, caso necessário, utilize:

```bash
python3 ex04_v1.py
```

```bash
python3 ex04_v2.py
```

---

## Exemplo de execução da V2

```text
==================================================
          SISTEMA DE CADASTRO DE PESSOAS
==================================================
--------------------------------------------------
                CADASTRO DE PESSOA
--------------------------------------------------
Digite a idade da pessoa: 25
Digite o sexo da pessoa [M/F]: M
Deseja continuar cadastrando pessoas? [S/N]: S
--------------------------------------------------
                CADASTRO DE PESSOA
--------------------------------------------------
Digite a idade da pessoa: 19
Digite o sexo da pessoa [M/F]: F
Deseja continuar cadastrando pessoas? [S/N]: N
==================================================
                  RELATÓRIO FINAL
==================================================
Quantidade de pessoas com mais de 18 anos: 2
Quantidade de homens cadastrados: 1
Quantidade de mulheres com menos de 20 anos: 1
==================================================
                 SISTEMA ENCERRADO
==================================================
```

---

## Testes funcionais

Os testes foram executados pelo estudante durante
o processo de desenvolvimento e validação das versões.

### Testes da V1

| Teste | Cenário | Resultado |
|---|---|---|
| 01 | Cadastro de várias pessoas | Aprovado |
| 02 | Limites de idade | Aprovado |
| 03 | Validação do sexo | Aprovado |
| 04 | Validação da continuidade e encerramento | Aprovado |

Resultado da V1:

- Testes realizados: 4
- Testes aprovados: 4
- Testes reprovados: 0
- Aproveitamento: 100%

### Testes da V2

| Teste | Cenário | Resultado |
|---|---|---|
| 01 | Entrada de letras | Aprovado |
| 02 | Entrada de número decimal | Aprovado |
| 03 | Entrada vazia | Aprovado |
| 04 | Entrada de idade negativa | Aprovado |
| 05 | Entrada de idade zero | Aprovado |
| 06 | Entrada de idade inteira positiva | Aprovado |
| 07 | Validação do sexo | Aprovado |
| 08 | Validação da continuidade | Aprovado |
| 09 | Contadores e limites de idade | Aprovado |
| 10 | Apresentação visual | Aprovado |

Resultado da V2:

- Testes realizados: 10
- Testes aprovados: 10
- Testes reprovados: 0
- Aproveitamento: 100%

### Resultado geral

| Versão | Realizados | Aprovados | Aproveitamento |
|---|---:|---:|---:|
| V1 | 4 | 4 | 100% |
| V2 | 10 | 10 | 100% |
| Total | 14 | 14 | 100% |

Os resultados correspondem aos cenários testados
e não representam cobertura integral do código.

---

## Limitações conhecidas

Apesar das melhorias implementadas na V2, existem
algumas limitações relacionadas ao escopo do exercício:

- O método isdigit() pode aceitar determinados
  caracteres Unicode, como o caractere ², que não
  podem ser convertidos diretamente por int().

- O programa não estabelece um limite máximo de idade,
  pois esse requisito não foi solicitado no enunciado.

- Os dados são armazenados temporariamente em variáveis
  e não são preservados após o encerramento do programa.

Essas limitações foram mantidas considerando o nível
de aprendizagem e os objetivos didáticos do exercício.

---

## Aprendizados adquiridos

Durante o desenvolvimento deste exercício, foram
consolidados conhecimentos relacionados a:

- Organização de estruturas condicionais.
- Diferença entre condições independentes e aninhadas.
- Impacto da indentação no fluxo de execução.
- Utilização de múltiplos contadores.
- Validação de dados antes da conversão de tipos.
- Identificação e correção de erros lógicos.
- Controle de fluxo com break e continue.
- Formatação de interfaces de terminal.
- Desenvolvimento incremental de software.
- Testes funcionais e de regressão.
- Documentação técnica de código.

Um dos principais aprendizados foi compreender
a sequência correta de processamento dos dados:

Entrada → Validação → Conversão → Processamento.

---

## Referência

Curso em Vídeo - Python 3 - Mundo 2

Professor: Gustavo Guanabara

Exercício 069 - Análise de Dados do Grupo

Site: https://www.cursoemvideo.com/

---

## Autor

Alexsandro Ferreira

Estudante de Engenharia de Software

GitHub: https://github.com/Alexsandrocf82

Projeto desenvolvido para fins educacionais,
com foco no aprimoramento da lógica de programação,
da linguagem Python e das boas práticas de
desenvolvimento de software.