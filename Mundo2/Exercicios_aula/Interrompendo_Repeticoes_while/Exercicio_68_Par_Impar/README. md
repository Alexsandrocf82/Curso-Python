
# 🎮 Exercício 068 - Jogo do Par ou Ímpar

## 📚 Sobre o exercício

Este exercício faz parte do curso Python 3 - Mundo 2,
da plataforma Curso em Vídeo, ministrado pelo professor
Gustavo Guanabara.

O objetivo é desenvolver um jogo de Par ou Ímpar entre
o usuário e o computador, utilizando estruturas de
repetição, condicionais, operadores matemáticos e
geração de números aleatórios.

O exercício foi desenvolvido em duas versões, demonstrando
a evolução do código por meio da identificação de erros,
validação de entradas e refatoração.

## 🎯 Objetivos

- Aplicar estruturas de repetição com while True.
- Utilizar estruturas condicionais if, elif e else.
- Trabalhar com operadores matemáticos e lógicos.
- Gerar números aleatórios utilizando randint().
- Utilizar contadores de vitórias consecutivas.
- Controlar o fluxo de execução com break e continue.
- Validar entradas de dados.
- Identificar e corrigir erros de execução.
- Desenvolver boas práticas de programação.

## ⚙️ Funcionamento do programa

1. O jogador informa um número inteiro.
2. O jogador escolhe Par (P) ou Ímpar (I).
3. O computador sorteia um número entre 0 e 10.
4. O programa calcula a soma dos dois números.
5. O resultado é classificado como par ou ímpar.
6. Caso o jogador vença, uma nova rodada é iniciada.
7. Caso o jogador perca, o jogo é encerrado.
8. O programa apresenta o total de vitórias consecutivas.

## 🚀 Evolução das versões

### Versão 1 - Implementação inicial

Arquivo: `ex03_v1.py`

Primeira implementação do jogo, utilizando os conceitos
estudados durante o curso.

Principais funcionalidades:

- Geração de números aleatórios.
- Validação da escolha entre Par e Ímpar.
- Verificação do resultado da soma.
- Contador de vitórias consecutivas.
- Encerramento do jogo após uma derrota.
- Controle do fluxo de execução.

Limitações identificadas:

- A conversão direta com int() pode gerar um ValueError
  quando o usuário informa uma entrada incompatível.
- Presença de estruturas condicionais redundantes.

### Versão 2 - Validação de entradas e refatoração

Arquivo: `ex03_v2.py`

Segunda versão desenvolvida a partir da identificação
de uma falha durante os testes da primeira versão.

Principais melhorias:

- Recebimento da entrada numérica inicialmente como string.
- Validação da entrada utilizando isdigit().
- Conversão para inteiro somente após a validação.
- Rejeição de letras comuns e entradas vazias.
- Rejeição de números negativos e decimais.
- Utilização de continue para reiniciar o laço.
- Remoção de estruturas condicionais redundantes.
- Melhoria na organização e robustez do código.

A lógica original do jogo foi preservada.

## 📊 Comparativo entre as versões

| Funcionalidade | V1 | V2 |
|---|---|---|
| Estrutura de repetição | Sim | Sim |
| Geração de números aleatórios | Sim | Sim |
| Contador de vitórias | Sim | Sim |
| Validação da escolha P/I | Sim | Sim |
| Validação da entrada numérica | Não | Sim |
| Tratamento de letras comuns | Não | Sim |
| Rejeição de números negativos | Não | Sim |
| Rejeição de entradas vazias | Não | Sim |
| Remoção de código redundante | Não | Sim |

## 🧠 Conceitos aplicados

- Variáveis e tipos de dados.
- Entrada e saída de dados.
- Estruturas condicionais.
- Estruturas de repetição.
- Operador de módulo (%).
- Operadores lógicos and e not.
- Contadores e acumuladores.
- Biblioteca random.
- Métodos de strings: strip(), upper() e isdigit().
- Controle de fluxo: break e continue.
- Validação de dados.
- Debugging.
- Refatoração de código.

## 🛠️ Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

## 📂 Estrutura dos arquivos

    Exercicio_68_Par_Impar/
    ├── ex03_v1.py
    ├── ex03_v2.py
    └── README.md

## ▶️ Como executar

É necessário possuir o Python 3 instalado.

Acesse o diretório do exercício pelo terminal e execute
um dos comandos abaixo.

### Executar a Versão 1

    python ex03_v1.py

### Executar a Versão 2

    python ex03_v2.py

Em sistemas Linux, utilize python3 caso o comando python
não esteja disponível.

## 💻 Exemplo de execução

    ====================
    VAMOS JOGAR PAR OU IMPAR
    ====================
    Digite um número: 5
    Par ou Impar[P/I]: P
    ====================
    Você jogou 5 e o computador 3. Total de 8 deu PAR
    ====================
    Você Venceu!
    ====================

### Exemplo de validação na Versão 2

    Digite um número: A
    Entrada Inválida. Digite um número inteiro não negativo

O programa retorna ao início do laço e solicita uma
nova entrada, sem encerrar a execução.

## 🧪 Cenários de teste

| Entrada ou situação | Resultado esperado na V2 |
|---|---|
| Letra A | Entrada rejeitada |
| Número decimal 5.5 | Entrada rejeitada |
| Entrada vazia | Entrada rejeitada |
| Número negativo -3 | Entrada rejeitada |
| Número inteiro 0 | Entrada aceita |
| Número inteiro 7 | Entrada aceita |
| Escolha P/I inválida | Reinício da rodada |
| Vitória | Incremento do contador |
| Derrota | Encerramento do jogo |


### Resultado dos testes funcionais

- Total de testes realizados: 9
- Testes aprovados: 9
- Testes reprovados: 0
- Taxa de aprovação: 100%
- Status: Versão 2 aprovada

Todos os cenários de teste previstos foram executados
com sucesso, atendendo aos requisitos funcionais
estabelecidos para esta versão.


## ⚠️ Limitações conhecidas

A Versão 2 utiliza o método isdigit() para validar
entradas numéricas comuns. Alguns caracteres Unicode
especiais podem passar por essa validação e ainda gerar
um erro durante a conversão com int().

O tratamento de exceções poderá ser explorado em
implementações futuras.

## 📈 Aprendizados adquiridos

O desenvolvimento deste exercício permitiu consolidar
os conhecimentos sobre estruturas de repetição,
condicionais e controle de fluxo.

A identificação de um ValueError durante os testes
motivou o desenvolvimento de uma segunda versão,
aplicando técnicas de validação de dados e refatoração.

Essa evolução reforça a importância dos testes,
da manutenção de código e da melhoria contínua
no desenvolvimento de software.

## 📖 Referência

- Curso em Vídeo - Python 3 - Mundo 2
- Professor Gustavo Guanabara
- Exercício 068 - Jogo do Par ou Ímpar
- https://www.cursoemvideo.com/

## 👨‍💻 Autor

Alexsandro Ferreira

Estudante de Engenharia de Software, em constante
desenvolvimento de competências em programação,
lógica computacional e desenvolvimento de software.

GitHub: https://github.com/Alexsandrocf82

---

📌 Exercício desenvolvido para fins educacionais,
como parte da minha jornada de aprendizagem em Python.
