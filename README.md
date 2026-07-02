# Projeto Calculadora: Shell Script & Python

Este projeto consiste em uma aplicação de calculadora funcional desenvolvida em automação Shell Script (.sh) e integrada com uma lógica estruturada em Python, além de seu respectivo arquivo executável.

## 📋 Sumário
- [Como Executar o Arquivo .sh](#como-executar-o-arquivo-sh)
- [Explicação do Código Shell Script](#explicação-do-código-shell-script)
- [Explicação do Código Python](#explicação-do-código-python)
- [Uso do Executável](#uso-do-executável)

---

## Como Executar o Arquivo .sh

Para rodar a versão em Shell Script do projeto, certifique-se de estar em um ambiente Unix (Linux ou macOS) ou utilizando o Git Bash no Windows. Siga os passos no terminal:

1. **Abra o terminal** na pasta onde o arquivo `calculadora.sh` está salvo.
2. **Conceda permissão de execução** para o arquivo utilizando o comando:
   ```bash
   chmod 744 calculadora.sh

## Explicação do Código Shell Script
O arquivo calculadora.sh realiza operações matemáticas básicas diretamente no terminal através dos seguintes blocos de lógica:

Entrada de Dados (read): O script solicita o primeiro número, o segundo número e o caractere que representa a operação matemática (+, -, *, /).

Estrutura de Seleção (case): Avalia a operação escolhida pelo usuário para definir qual cálculo será executado:

Soma, Subtração e Multiplicação: Realizadas através da expansão aritmética do Shell $((num1 operacao num2)).

Divisão com Validação: Uma condicional if verifica se o segundo número é igual a zero (-eq 0). Se for, retorna uma mensagem de erro; caso contrário, efetua a divisão.

Tratamento de Erros (*): Se qualquer outro caractere inválido for digitado, o script informa "Operação inválida!".

Exibição do Resultado (echo): Imprime na tela o valor final armazenado na variável $resultado.

## Explicação do Código Python
O script em Python (calculadora.py) implementa uma calculadora interativa com validações de entrada e controle de fluxo condicional estruturado.

Lógica e Estrutura do Código:
Validação do Primeiro Operando:

O programa solicita o num1 convertendo a entrada para um número inteiro (int).

Uma estrutura condicional (if num1 > 0:) valida se o número é estritamente maior que zero. Caso não seja, o script cai na cláusula else final, exibindo a mensagem: "Impossivel fazer qualquer operação com zero."

Captura de Dados Adicionais:

Uma vez validado que num1 é maior que zero, o programa avança para solicitar o segundo operando (num2) e a operação matemática desejada (opera).

Processamento das Operações (if / elif / else):

Soma (+), Subtração (-) e Multiplicação (*): O script avalia a string digitada e imprime diretamente o resultado da operação aritmética correspondente.

Divisão (/): Antes de realizar o cálculo, o código executa uma validação interna importante (if num2 != 0:). Se o segundo número for diferente de zero, a divisão é calculada e exibida. Se for zero, o programa previne um erro do sistema imprimindo de forma segura: "Erro: Divisão por zero não é permitida."

Operação Inválida: Se o usuário digitar qualquer caractere que não corresponda aos operadores mapeados, o sistema retorna "Operação inválida."

## Uso do Executável
Para usuários que não possuem o ambiente Python ou o terminal Shell configurado, disponibilizamos o arquivo executável compilado na raiz do repositório.

Basta efetuar o download do arquivo executável correspondente (CalculadoraMarcusZ.exe).

No Windows, clique duas vezes para abrir a interface em linha de comando.

No Linux/macOS, execute-o de forma análoga ao arquivo .sh.
