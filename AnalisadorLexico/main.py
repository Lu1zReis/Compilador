# definicoes
TOKENS = [
    "FUNC", "INT", "REAL", "STRING", "LISTA", "SE", "PODESER", 
    "SENAO", "PARA", "ENQUANTO", "RETORNO", "JUROU", "CERTIN", "CONST",
    "OP_LOGICO", "OP_NUMERICO", "OP_RELACIONAL",
    "IDENT", "DEL", "STRING_VAL", "LISTA_VAL", "INT_VAL", "REAL_VAL", "CLASSE"
]

# palavras-chave

delimitadores = [",", ";", "(", ")", "{", "}", '[', ']']
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

def isInt(buffer): #L: adicionei a função de num inteiros
    return buffer.isdigit()

def isString(buffer):  #L: adicionei a função para reconhecer strings '>exemplo<'
    return buffer.startswith('>') and buffer.endswith('<')

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

def main(nome_arquivo):
    codigo = open(nome_arquivo, "r")
    buffer = ""

    string_current = False
    for linha in codigo:
        for carac in linha:
            carac_unico_especial = carac in delimitadores or carac in operadores_logic or carac in operadores_relac or carac in operadores_aritm
            if carac == "'" or carac == '"':
                string_current = not string_current
            if isEnd(carac) or (carac_unico_especial and not string_current):
                # tentar classificar o buffer antes de limpar
                if buffer:
                    if buffer == "func":
                        add(buffer, "FUNC")
                    elif isClass(buffer):
                        add(buffer, "CLASSE")
                    elif isIdent(buffer):
                        add(buffer, "IDENT")  
                    elif isFloat(buffer):
                        add(buffer, "REAL")
                    elif isString(buffer):
                        add(buffer, "STRING")
                    else:
                        add(buffer, "ERRO")

                    # sempre ira limpar
                    string_current = False
                    buffer = ""

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
        elif isComentario(buffer):
            add(buffer, "COMENTARIO")
        else:
            add(buffer, "ERRO")

    if comentario_current:
        print("Erro léxico: comentário não fechado (faltando $ no final).")
        add(buffer, "ERRO")

    display()

main()
