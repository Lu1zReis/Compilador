# definicoes
TOKENS = [
    "FUNC", "INT", "REAL", "STRING", "LISTA", "SE", "PODESER", 
    "SENAO", "PARA", "ENQUANTO", "RETORNO", "JUROU", "CERTIN", "CONST",
    "OP_LOGICO", "OP_NUMERICO", "OP_RELACIONAL",
    "IDENT", "DEL", "STRING_VAL", "LISTA_VAL", "INT_VAL", "REAL_VAL", "CLASSE"
]

delimitadores = [",", ";", "(", ")", "{", "}"]
operadores_logic = ["&", "|", "!"]
operadores_aritm = ["+", "-", "*", "/", "%"]
operadores_relac = ["=", ">", "<"]

# variavel global
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
    return size > 1 and size <= 24 and buffer[0] == buffer[0].upper() and buffer[0].isalpha()

def isFloat(buffer):
    # "10.2"
    tevePontuacao = False
    for digit in buffer:
        if not digit.isdigit() and digit != '.':
            return False
        elif digit == '.':
            tevePontuacao = True
    
    if tevePontuacao:
        return True
    return False

def isDelim(buffer):
    return buffer in delimitadores

def isOpLogic(buffer):
    return buffer in operadores_logic

def isOpRelac(buffer):
    return buffer in operadores_relac

def isOpAritm(buffer):
    return buffer in operadores_aritm

#############################################

# funcoes auxiliares
def isEnd(caractere):
    return caractere in [' ', '\n', '\t']

def add(lexema, token):
    resultado.append((token, lexema))

def display():
    print("<TOKEN, LEXEMA>")
    for token, lexema in resultado:
        print(f"<{token}, {lexema}>")

#############################################

def main():
    codigo = "/Classe_01() {1.0 + 10.2;}"
    buffer = ""

    for i, carac in enumerate(codigo):
        carac_unico_especial = carac in delimitadores or carac in operadores_logic or carac in operadores_relac or carac in operadores_aritm
        if isEnd(carac) or carac_unico_especial:
            # tentar classificar o buffer antes de limpar
            if buffer:
                if isClass(buffer):
                    add(buffer, "CLASSE")
                elif isIdent(buffer):
                    add(buffer, "IDENT")  
                elif isFloat(buffer):
                    add(buffer, "REAL")
                else:
                    add("Erro", "ERRO")

                # sempre ira limpar
                buffer = ""

            # tratando quando é só um caractere
            if isDelim(carac):
                add(carac, "DEL")
            elif isOpLogic(carac):
                add(carac, "OP_LOGIC")
            elif isOpRelac(carac):
                add(carac, "OP_RELAC")
            elif isOpAritm(carac):
                add(carac, "OP_ARITM")
                
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
