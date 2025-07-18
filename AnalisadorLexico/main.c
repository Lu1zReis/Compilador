#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 1000
#define TOKEN_SIZE 16

enum Tokens {
    // PALAVRAS RESERVADAS
    VOID = 0,
    IF = 1,
    ELSE = 2,
    WHILE = 3,
    FOR = 4,
    INT = 5,
    CHAR = 6,
    FLOAT = 7,
    // OPERADORES
    OP_LOGIC = 8,
    OP_NUMBER = 9,
    OP_REL = 10,
    // VARIAVEIS E VALORES
    VAR = 11,
    DEL = 12,
    CHAR_VAL = 13,
    INT_VAL = 14,
    FLOAT_VAL = 15
};

int endToken(char c) {
    if (c == '\n' || c == ' ' || c == '\0') {
        return 1;
    }
    return 0;
}

int isOpLogic(char *c, int start, int end) {

}
int isOpNumber(char *c, int start, int end) {}
int isOpRel(char *c, int start, int end) {}
int isVar(char *c, int start, int end) {}
int isDel(char *c, int start, int end) {}
int isReal(char *c, int start, int end) {}
int isInteger(char *c, int start, int end) {}
int isString(char *c, int start, int end) {}

// funcao para adicionar o lexema atual na lista de lexema
// passamos o token para saber onde aquele lexema ira cair
void add(char lexe[][BUFFER_SIZE], char *c, int start, int end, int token) {
    int i, j, start_lexe = strlen(lexe[token]);

    for (i = start, j = 0; i < end; i++, j++) {
        lexe[token][start_lexe + j] = c[i];
    }
    lexe[token][start_lexe + j] = '\0';
}

void display_tokens(char lexe[][BUFFER_SIZE]) {
    for (int i = 0; i < TOKEN_SIZE; i++) {
        if (lexe[i][0] != '\0') {
            printf("Token %d: %s\n", i, lexe[i]);
        }
    }
}

int main () {

    // exemplo
    char codigo[] = "int j = 0; for (j = 0; j < 10; j++) printf(\"teste %d\", &j); return 0;";


    // variavel para guardar cada lexema
    char buffer[BUFFER_SIZE];
    // variavel para guardar em cada token os seus respectivos lexemas
    char lexemas[TOKEN_SIZE][BUFFER_SIZE] = {0};

    int i, j, start = 0;

    for (i = 0; i < sizeof(codigo)/sizeof(char); i++) {
        buffer[i] = codigo[i];
        // verificar se acabou
        if (endToken(codigo[i])) {
            buffer[i+1] = '\0';
            // verificar qual token o último buffer pertence
            if (isOpLogic(buffer, start, i+1)) {
                add(lexemas, buffer, start, i+2, OP_NUMBER);
            }


            // vamos definir um novo inicio
            start = i + 2;
            i = start;
        }
    }

    return 0;
}