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
| Exemplo                            | Token                              | Explicação                        |
| ---------------------------------- | ---------------------------------- |---------------------------------- |
| -                                  | FUNC                               | Inicio de função pode começar com '#' ou a palavra reservada 'func'   | 
| -                                  | CLASSE                             | Inicio de classe pode começar com '/' ou a palavra reservada 'Classe' |
| -                                  | IDENT                              | + [a-zA-Z0-9_], máx. 24 caracteres                                    |
| int                                | INT                                | Palavra chave*                                                        |
| real                               | REAL                               | Palavra chave*                                                        |
| string                             | STRING                             | Palavra chave*                                                        |
| Colecao                            | COLECAO                            | Palavra chave*                                                        |
| const                              | CONST                              | Palavra chave*                                                        |
| se, podeser, senao                 | SE, PODESER, SENAO                 | Palavra chave*                                                        |
| para, em, de, ate                  | PARA, EM, DE, ATE                  | Palavra chave*                                                        |
| enquanto, faca                     | ENQUANTO, FACA                     | Palavra chave*                                                        |
| jurou, certin                      | JUROU, CERTIN                      | Palavra chave*                                                        |
| este                               | ESTE                               | Palavra chave*                                                        |
| publico, privado                   | MODIFICADOR                        | Palavra chave*                                                        |
| ler                                | LER                                | Palavra chave*                                                        |
| escreva                            | ESCREVA                            | Palavra chave*                                                        |
| retorno                            | RETORNO                            | Palavra chave*                                                        |

---
## **Operadores e Delimitadores**
| Tipo        | Exemplos       | Token     | 
| ----------- | -------------- | --------- | 
| Aritméticos | +, -, \*, /, % | OP\_ARITM | 
| Relacionais | =, >, <        | OP\_RELAC |       
| Lógicos     | &, \|,  \!     | OP\_LOGIC |
| Delimitador | , ; ( ) { } \[ ] . @ | DEL   |

---
Explicando
