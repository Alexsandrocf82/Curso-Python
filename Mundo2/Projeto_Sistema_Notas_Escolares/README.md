
# Projeto 08 — Sistema de Controle de Notas Escolares

## Sobre o projeto

Sistema desenvolvido em Python para cadastrar alunos, calcular
médias individuais, classificar o desempenho escolar e calcular
a média geral de uma turma.

O projeto integra meu processo de formação em programação
e Engenharia de Software, aplicando os conhecimentos adquiridos
durante o curso Python 3 — Mundo 2, do Curso em Vídeo.

Data do desenvolvimento original: 08/11/2026.

## Objetivos

- Consolidar os fundamentos da lógica de programação.
- Aplicar estruturas condicionais e de repetição.
- Desenvolver habilidades com contadores e acumuladores.
- Implementar validação de dados.
- Praticar o versionamento de código com Git e GitHub.

## Funcionalidades

- Cadastro de múltiplos alunos.
- Entrada de duas notas por aluno.
- Cálculo da média individual.
- Classificação do desempenho escolar.
- Contagem dos alunos cadastrados.
- Cálculo da média geral da turma.
- Exibição dos resultados individuais e coletivos.
- Validação do intervalo das notas na versão 2.0.

## Regras de negócio

| Média | Situação |
|---|---|
| Maior ou igual a 7,0 | Aprovado |
| Maior ou igual a 5,0 e menor que 7,0 | Recuperação |
| Menor que 5,0 | Reprovado |

Na versão 2.0, as notas numéricas devem estar entre
0 e 10, inclusive.

## Evolução do projeto

### Versão 1.0 — Estrutura básica

Arquivo: `notas_v1_estrutura_basica.py`

- Cadastro de múltiplos alunos utilizando while.
- Cálculo das médias individuais.
- Classificação do desempenho escolar.
- Implementação de contador e acumulador.
- Cálculo da média geral da turma.
- Proteção contra divisão por zero.

### Versão 2.0 — Validação das notas

Arquivo: `notas_v2_validacao.py`

- Preservação das funcionalidades da versão anterior.
- Validação do intervalo numérico das notas.
- Implementação de estruturas de repetição aninhadas.
- Utilização do operador lógico or.
- Solicitação de novas notas quando o valor informado
  estiver fora do intervalo permitido.

## Conceitos de programação aplicados

- Variáveis e tipos de dados.
- Entrada e saída de dados.
- Operadores aritméticos.
- Operadores relacionais.
- Operadores lógicos.
- Estruturas condicionais: if, elif e else.
- Estruturas de repetição: while.
- Estruturas de repetição aninhadas.
- Contadores e acumuladores.
- Formatação de strings com f-strings.
- Validação de dados.
- Comentários e documentação de código.

## Tecnologias e ferramentas

- Python 3
- Visual Studio Code
- Git
- GitHub
- GitHub Desktop
- Markdown

## Estrutura do projeto

    Projeto_Sistema_Notas_Escolares/
    ├── notas_v1_estrutura_basica.py
    ├── notas_v2_validacao.py
    └── README.md

## Como executar

É necessário ter o Python 3 instalado no computador.

Abra o terminal na pasta do projeto e execute:

### Versão 1.0

```bash
python notas_v1_estrutura_basica.py
```

### Versão 2.0

```bash
python notas_v2_validacao.py
```

Não é necessária a instalação de bibliotecas externas.

## Testes funcionais

Os testes manuais foram realizados em 15/11/2026.

| Versão | Cenário de teste | Resultado |
|---|---|---|
| V1 | Cadastro individual | Aprovado |
| V1 | Cadastro de múltiplos alunos | Aprovado |
| V2 | Funcionamento básico | Aprovado |
| V2 | Validação de notas fora do intervalo | Aprovado |
| V2 | Valores-limite e múltiplos alunos | Aprovado |

Total: 5 cenários de testes aprovados.

## Limitações atuais

- Não possui armazenamento permanente dos dados.
- Não possui tratamento de entradas não numéricas.
- Não possui validação de nomes vazios.
- Não possui validação completa da opção de continuidade.
- Funciona exclusivamente por meio do terminal.

## Possibilidades de evolução

- Implementação de tratamento de exceções.
- Validação completa dos dados de entrada.
- Armazenamento de alunos utilizando listas e dicionários.
- Modularização do código utilizando funções.
- Persistência de dados em arquivos.
- Implementação de relatórios estatísticos.
- Desenvolvimento de interface gráfica.
- Integração futura com banco de dados.

## Aprendizados

O desenvolvimento deste projeto permitiu consolidar o uso
de estruturas condicionais, estruturas de repetição,
contadores e acumuladores, além de compreender a importância
da validação de dados para a construção de sistemas mais
consistentes.

A manutenção de duas versões demonstra minha evolução
progressiva no desenvolvimento de software.

## Autor

**Alexsandro Ferreira**

Professor e estudante de Engenharia de Software.

GitHub: https://github.com/Alexsandrocf82

---

Projeto desenvolvido para fins educacionais como parte
do meu processo contínuo de aprendizagem em programação.
