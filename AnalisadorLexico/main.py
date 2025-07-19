# definicoes
TOKENS = [
    "FUNC", "INT", "REAL", "STRING", "LISTA", "SE", "PODESER", 
    "SENAO", "PARA", "ENQUANTO", "RETORNO", "JUROU", "CERTIN", "CONST",
    "OP_LOGICO", "OP_NUMERICO", "OP_RELACIONAL",
    "VAR", "DEL", "STRING_VAL", "LISTA_VAL", "INT_VAL", "REAL_VAL", "CLASSE"
]

delimitadores = [",", ";", "(", ")", "{", "}"]
operadores_logic = ["&", "|", "!"]
operadores_aritm = ["+", "-", "*", "/", "%", "**"]
operadores_relac = ["=", ">", "<"]

resultado = []

# regras de cada token
def isIdent(buffer):
    if ((buffer[0].isalpha() and buffer[0] == buffer[0].lower()) or buffer[0] == '@') and len(buffer) <= 12:
        for carac in buffer[1:]:
            if carac.isalpha() or carac.isdigit() or carac == '_':
                pass
            else:
                return False    
        return True

def isClass(buffer):
    size = len(buffer)
    return size > 2 and size <= 24 and buffer[0] == '/'

def isDelim(buffer):
    return buffer in delimitadores

def isOpLogic(buffer):
    return buffer in operadores_logic

def isOpRelac(buffer):
    return buffer in operadores_relac

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
    codigo = "/Classe_01() {teste > teste2;}"
    buffer = ""

    for i, carac in enumerate(codigo):
        carac_unico = carac in delimitadores or carac in operadores_logic or carac in operadores_relac
        if isEnd(carac) or carac_unico:
            # lendo caracteres que precisam ser adicionados no buffer para funcionar
            entrarParaClassificar = True
            if carac == '/':
                buffer += carac
                entrarParaClassificar = False

            # tentar classificar o buffer antes de limpar
            if buffer and entrarParaClassificar:
                if isClass(buffer):
                    add(buffer, "CLASSE")
                elif isIdent(buffer):
                    add(buffer, "IDENT")  # token padrão
                else:
                    add("Erro", "ERRO")
                buffer = ""

            # tratando quando é só um caractere
            if isDelim(carac):
                add(carac, "DEL")
            elif isOpLogic(carac):
                add(carac, "OP_LOGIC")
            elif isOpRelac(carac):
                add(carac, "OP_RELAC")
        else:
            buffer += carac

    # se restar algo
    if buffer:
        if isClass(buffer):
            add(buffer, "CLASSE")
        elif isIdent(buffer):
            add(buffer, "IDENT")  # token padrão 

    display()

main()
