# Compilador
Repositório para o projeto de Compiladores

# 🧠 Analisador Léxico – Zlang

Este projeto é um **analisador léxico** feito em Python para uma linguagem fictícia inspirada no vocabulário da **geração Z**, em português, combinando características de linguagens como **Python** e **C**.

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
## **Demonstrando alguns exemplos**
### Além dos exemplos contidos abaixo neste `README.md`, há outros arquivos de exemplo na pasta `AnalisadorLexico/exemplos`

### **Coleções**
- - Uma coleção é um tipo de lista/matriz heterogênea.
  - Definindo:
  - - ```
        Colecao lista;
      ```
  - Atribuindo valor:
  - - ```
        lista = [1, "string", [2.10, 33]];
        lista.adicionar(variavel); $ adiciona no fim da coleção
        lista.inserir("teste", "string"); $ este método procura o valor passado pelo segundo parâmetro e substitui pelo primeiro parâmetro
        lista[0] = 2; $ sobrescrevendo valor
      ```
  - Removendo valor:
  - - ```
      lista.removePosicao(2); $ remove o elemento da posição 2
      lista.removeUltimo(); $ remove último elemento
      ```
  - Tamanho de uma lista:
  - - ```
      lista.tamanho(); $ retorna o tamanho da lista
      ```
### **Classes**
- Para definir uma classe, podemos usar '/' ou a palavra reservada 'Classe':
```
/Classe Pessoa() {
  privado string nome;
  privado int idade;

  publico #definirDados(string nome, int idade) {
    este.nome = nome;
    este.idade = idade;
  }

  publico #mostrarDados() {
    escreva("Nome:", este.nome);
    escreva("Idade:", este.idade);
  }
}
```
- Criando instância e usando métodos:
```
@pessoa = Pessoa();
pessoa.definirDados("Lucas", 30);
pessoa.mostrarDados();
```
### **Funções**
- Uma função pode começar com '#' ou com a palavra reservada 'func':
```
#somar(int a, int b) {
  retorno a + b;
}

func ehMaior(int x, int y) {
  se x > y {
    retorno certin;
  } senao {
    retorno jurou;
  }
}
```
- Chamando as funções:
```
escreva(somar(10, 5));
escreva(ehMaior(10, 5));
```

### **Laços**
- **Para**
- - Uma das estruturas de repetição que podemos utilizar é o '**para**'. Ele pode tanto percorrer por posição.
   ```
      para i de 0 até lista.tamanho() {
        escreva(i);
      }  
    ```
- - ou interar sobre uma lista.
   ```
      para item em lista {
        escreva(item);
      }  
    ```
- **Enquanto**
- - Outra estrutura de repetição que podemos utilizar é o '**enquanto**'. 
   ```
      enquanto (lista.tamanho() != 0) {
         escreva(lista[lista.tamanho()-1])
         lista.removeUltimo();
      }  
    ```
---

## **⚙ Como rodar**
1. Clone ou baixe o projeto.
2. Coloque seu código de teste no arquivo exemplo.txt.
3. Vá até a pasta 'AnalisadorLexico' e Execute:
```plaintext
  python main.py
```
