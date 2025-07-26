# Compilador
Repositório para o projeto de Compiladores

# 🧠 Analisador Léxico – PortuLang

Este projeto é um **analisador léxico** feito em Python para uma linguagem fictícia inspirada no **português**, combinando características de linguagens como **Python** e **C**.

Ele transforma um código fonte em uma sequência de **tokens**, que descrevem as partes significativas do programa: palavras reservadas, identificadores, operadores, literais etc.

---

## ✅ **Como funciona**

O analisador percorre o código fonte caractere por caractere, construindo "buffers" de texto. Quando encontra um espaço, delimitador ou operador, verifica:
- Se o buffer acumulado é um número, identificador, palavra reservada, etc.
- Se o caractere atual é um delimitador, operador ou outro símbolo especial.

Ele gera tokens no formato (exemplo):
```plaintext
<TOKEN, LEXEMA>
<FUNC, #pegarValor>
<INT, int>
<IDENT, a>
<OP_ARITM, +>
```

---
## **Palavras Reservadas e Valores**
| Exemplo                            | Token                              | Explicação                                                                                    |
| ---------------------------------- | ---------------------------------- |-----------------------------------------------------------------------------------------------|
| -                                  | FUNC                               | Inicio de função pode começar com '#' ou a palavra reservada 'func' antes do identificador.   | 
| -                                  | CLASSE                             | Inicio de classe pode começar com '/' ou a palavra reservada 'Classe' antes do identificador. |
| -                                  | IDENT                              | + [a-zA-Z0-9_], máx. 12 caracteres.                                                           |
| -                                  | COMENTARIO                         | Um comentário deve começar com '$' e terminar com uma quebra de linha '\n' ou um outro '$'.   |
| int                                | INT                                | Define o tipo de um identificador.                                                            |
| real                               | REAL                               | Define o tipo de um identificador.                                                            |
| string                             | STRING                             | Define o tipo de um identificador.                                                            |
| Colecao                            | COLECAO                            | Define o tipo de um identificador.                                                            |
| const                              | CONST                              | Define que o identificador terá valor fixo.                                                   |
| se, podeser, senao                 | SE, PODESER, SENAO                 | *                                                                                             |
| para, em, de, ate                  | PARA, EM, DE, ATE                  | *                                                                                             |
| enquanto, faca                     | ENQUANTO, FACA                     | *                                                                                             |
| jurou, certin                      | JUROU, CERTIN                      | Resultados booleano para Falso (jurou) e Verdadeiro (certin).                                 |
| este                               | ESTE                               | Indica que um atributo ou método pertence aquela classe.                                      |
| publico, privado                   | MODIFICADOR                        | Muda a visibilidade de um membro de uma classe.                                               |
| ler                                | LER                                | Entrada externa do teclado.                                                                   |
| escreva                            | ESCREVA                            | Exibir o conteúdo no prompt do usuário.                                                       |
| retorno                            | RETORNO                            | Retorna algum valor.                                                                             |

---
## **Operadores e Delimitadores**
| Tipo        | Exemplos               | Token     | 
| ----------- | ---------------------- | --------- | 
| Aritméticos | +, -, \*, /, %         | OP\_ARITM | 
| Relacionais | =, >, <                | OP\_RELAC |       
| Lógicos     | &, \|,  \!             | OP\_LOGIC |
| Delimitador | , ; ( ) { } \[ ] . @ # | DEL       |

---
## **⚙ Como rodar**
1. Clone ou baixe o projeto.
2. Coloque seu código de teste no arquivo exemplo.txt.
3. Vá até a pasta 'AnalisadorLexico' e Execute:
```plaintext
  python main.py
```
