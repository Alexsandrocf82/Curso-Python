# Exercício 059 — Menu Interativo em Python

## 📌 Sobre o exercício

Este exercício faz parte do **Curso de Python — Mundo 2**, ministrado pelo professor Gustavo Guanabara, do Curso em Vídeo.

O objetivo é desenvolver um programa que receba dois números inteiros e apresente um menu interativo, permitindo ao usuário realizar diferentes operações até escolher a opção de encerramento.

O exercício foi desenvolvido em **três versões**, registrando a evolução do raciocínio lógico, a organização do código e a implementação de melhorias na interação com o usuário.

## 🎯 Funcionalidades

O programa apresenta cinco opções:

1. **Somar:** calcula a soma dos dois números.
2. **Multiplicar:** calcula o produto dos números.
3. **Maior:** identifica o maior valor ou informa quando são iguais.
4. **Novos números:** permite substituir os valores informados.
5. **Sair do programa:** encerra a execução.

O menu permanece disponível enquanto o usuário não escolher a opção de saída.

## 🚀 Evolução das versões

### Versão 1 — Implementação inicial

**Arquivo:** `ex059_v1.py`

- Construção do menu utilizando `print()` com múltiplas linhas.
- Implementação das cinco opções com `if`, `elif` e `else`.
- Utilização do `while` para repetir o menu.
- Comparação de valores, incluindo o tratamento de números iguais.
- Mensagem para opções numéricas inexistentes.

### Versão 2 — Reorganização do menu

**Arquivo:** `ex059_v2.py`

- Apresentação das opções por meio de comandos `print()` individuais.
- Melhoria na organização visual do menu.
- Preservação das operações e da estrutura de repetição da primeira versão.

### Versão 3 — Validação da opção do menu

**Arquivo:** `ex059_v3.py`

- Implementação de `.strip()` para remover espaços no início e no final da entrada.
- Utilização de `.isdigit()` para verificar se a opção contém apenas dígitos.
- Conversão para `int` somente após a verificação.
- Tratamento de entradas não numéricas sem interromper o programa com `ValueError`.

### Melhorias aplicadas às três versões

Após o desenvolvimento inicial, foram acrescentados:

- `from time import sleep` para importar a função de pausa.
- `print('=-=' * 10)` para separar visualmente as operações.
- `sleep(2)` para aguardar dois segundos antes da próxima interação ou do encerramento.

Essas melhorias tornam a utilização do programa mais organizada, sem modificar as operações principais.

## 🧠 Conceitos de Python utilizados

- Entrada e saída de dados com `input()` e `print()`.
- Conversão de tipos com `int()`.
- Estruturas condicionais `if`, `elif` e `else`.
- Estrutura de repetição `while`.
- Operadores aritméticos e relacionais.
- Validação básica de entradas com `.strip()` e `.isdigit()`.
- Importação de módulos da biblioteca padrão.
- Controle de tempo de execução com `sleep()`.

## 🧪 Testes e validação

Os cenários definidos para testar a Versão 3 incluem:

- Soma e multiplicação.
- Identificação do maior número.
- Comparação de números iguais.
- Substituição dos valores.
- Encerramento do programa.
- Opções inexistentes.
- Entradas com letras, espaços ou vazias no menu.
- Operações com zero e números negativos.
- Execução de várias operações consecutivas.

**Limitação conhecida:** a Versão 3 valida a opção escolhida no menu, mas a entrada dos dois números continua utilizando diretamente `int(input(...))`. Portanto, informar texto não numérico nesses campos pode gerar `ValueError`.

## 📂 Estrutura dos arquivos

```text
Exercicio_059_Menu_Interativo/
├── ex059_v1.py
├── ex059_v2.py
├── ex059_v3.py
└── README.md
```

## ▶️ Como executar

É necessário ter o Python 3 instalado.

Abra o terminal na pasta do exercício e execute a versão desejada:

**Versão 1:**
```bash
python ex059_v1.py
```

**Versão 2:**
```bash
python ex059_v2.py
```

**Versão 3:**
```bash
python ex059_v3.py
```

Em alguns sistemas Linux, o comando utilizado pode ser `python3` em vez de `python`.

## 📚 Aprendizados

O desenvolvimento das três versões permitiu consolidar o uso de estruturas condicionais e de repetição em um programa interativo.

Também possibilitou compreender a importância da organização da saída no terminal e da validação de dados antes da conversão de tipos.

A manutenção das três versões permite acompanhar a evolução do código, desde a implementação inicial até a introdução de uma validação mais segura para o menu.

## 🤝 Apoio ao desenvolvimento

Exercício desenvolvido como parte dos estudos de Python do Curso em Vídeo, com acompanhamento de inteligência artificial para revisão de código, análise de testes e organização da documentação.

A resolução e as melhorias foram trabalhadas progressivamente, com foco no desenvolvimento do raciocínio lógico e na compreensão dos conceitos utilizados.