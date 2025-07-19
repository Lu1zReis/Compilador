# definicoes
TOKENS = [
    "FUNC", "INT", "REAL", "STRING", "LISTA", "SE", "PODESER", 
    "SENAO", "PARA", "ENQUANTO", "RETORNO", "JUROU", "CERTIN", "CONST",
    "OP_LOGICO", "OP_NUMERICO", "OP_RELACIONAL",
    "VAR", "DEL", "STRING_VAL", "LISTA_VAL", "INT_VAL", "REAL_VAL", "CLASSE"
]

delimitadores = [",", ";", "(", ")", "{", "}", "/"]
operadores_logic = []
operadores_aritm = []
operadores_relac = []

resultado = []

# regras de cada token
def isClass(buffer):
    size = len(buffer)
    return size > 2 and size <= 24 and buffer[0] == '/' and buffer.endswith("()")

def isDelim(buffer):
    return buffer in delimitadores

# funcoes auxiliares
def isEnd(caractere):
    return caractere in [' ', '\n', '\t']

def add(lexema, token):
    resultado.append((token, lexema))

def display():
    print("<TOKEN, LEXEMA>")
    for token, lexema in resultado:
        print(f"<{token}, {lexema}>")


def main():
    codigo = "/Classe_01() teste;"
    buffer = ""

    for i, carac in enumerate(codigo):
        if isEnd(carac) or carac in delimitadores:
            # tentar classificar o buffer antes de limpar
            if buffer:
                if isClass(buffer):
                    add(buffer, "CLASSE")
                else:
                    add(buffer, "VAR")  # token padrão
                buffer = ""

            # agora trata o delimitador
            if isDelim(carac):
                add(carac, "DEL")
        else:
            buffer += carac

    # se restar algo
    if buffer:
        if isClass(buffer):
            add(buffer, "CLASSE")
        else:
            add(buffer, "VAR")  

    display()

main()
