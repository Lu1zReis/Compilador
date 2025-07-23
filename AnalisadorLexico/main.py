# definicoes
TOKENS = [
    "FUNC", "INT", "REAL", "STRING", "SE", "PODESER", 
    "SENAO", "PARA", "ENQUANTO", "RETORNO", "JUROU", "CERTIN", "CONST",
    "OP_LOGICO", "OP_NUMERICO", "OP_RELACIONAL",
    "IDENT", "DEL", "STRING_VAL", "COLECAO_VAL", "INT_VAL", "REAL_VAL", "CLASSE", "COMENTARIO"
]

# Já feitos: STRING_VAL, REAL_VAL, DEL, CLASSE, IDENT, OP_LOGICO, OP_NUMERICO, OP_RELACIONAL

delimitadores = [",", ";", "(", ")", "{", "}", '[', ']']
operadores_logic = ["&", "|", "!"]
operadores_aritm = ["+", "-", "*", "/", "%"]
operadores_relac = ["=", ">", "<"]

# dicionario para as palavras reservadas
palavras_reservadas = {
    "func": "FUNC",
    "int": "INT",
    "real": "REAL",
    "string": "STRING",
    "lista": "LISTA",
    "matriz": "MATRIZ",
    "se": "SE",
    "podeser": "PODESER",
    "senao": "SENAO",
    "para": "PARA",
    "enquanto": "ENQUANTO",
    "retorno": "RETORNO",
    "jurou": "JUROU",
    "certin": "CERTIN",
    "const": "CONST"
}

# variavel global
resultado = []

# regras de cada token
def isString(buffer):
    # String deve começar e terminar com aspas simples ou duplas
    return (buffer.startswith('"') and buffer.endswith('"')) or (buffer.startswith("'") and buffer.endswith("'"))

def isFunc(buffer):
    if not (buffer.startswith('#') and buffer.endswith('()')):
        return False
    nome = buffer[1:-2]
    return 1 <= len(nome) <= 24 and all(c.isalnum())

def isIdent(buffer):
    if buffer[0].isalpha() and buffer[0] == buffer[0].lower() and len(buffer) <= 12:
        return all(c.isalpha() or c.isdigit() or c == '_' for c in buffer[1:])
    return False

def isClass(buffer):
    size = len(buffer)
    return size > 1 and size <= 24 and buffer[0] == buffer[0].upper() and buffer[0].isalpha()

def isFloat(buffer):
    if buffer.count('.') == 1:
        parte1, parte2 = buffer.split('.')
        return parte1.isdigit() and parte2.isdigit()
    return False

def isInt(buffer):
    return buffer.isdigit()

def isDelim(buffer):
    return buffer in delimitadores

def isOpLogic(buffer):
    return buffer in operadores_logic

def isOpRelac(buffer):
    return buffer in operadores_relac

def isOpAritm(buffer):
    return buffer in operadores_aritm

def isComentario(buffer):
    return buffer.startswith('$') and buffer.endswith('$') and len(buffer) >= 2

def isPalavraReservada(buffer):
    return buffer in palavras_reservadas

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
    

    buffer = ""

    string_current = False
    string_delim = ""  # Qual delimitador abriu a string (' ou ")
    comentario_current = False 

    for i, carac in enumerate(codigo):
        carac_unico_especial = carac in delimitadores or carac in operadores_logic or carac in operadores_relac or carac in operadores_aritm
        
        # Controle de strings: alterna ao encontrar ' ou "
        if carac in ["'", '"']:
            if not string_current:
                string_current = True
                string_delim = carac
                buffer += carac
                continue
            elif string_current and carac == string_delim:
                buffer += carac
                string_current = False
                continue

        # Controle de comentários
        if carac == '$':
            if not comentario_current:
                comentario_current = True
                buffer = '$'
                continue
            else:
                buffer += '$'
                comentario_current = False
                if isComentario(buffer):
                    add(buffer, "COMENTARIO")
                else:
                    print(f"Erro léxico: comentário malformado -> {buffer}")
                    add(buffer, "ERRO")
                buffer = ""
                continue

        if comentario_current:
            buffer += carac
            continue

        if isEnd(carac) or (carac_unico_especial and not string_current):
            # tentar classificar o buffer antes de limpar
            if buffer:
                if isPalavraReservada(buffer):
                    add(buffer, palavras_reservadas[buffer])
                elif isFunc(buffer):
                    add(buffer, "FUNC")
                elif isClass(buffer):
                    add(buffer, "CLASSE")
                elif isIdent(buffer):
                    add(buffer, "IDENT")  
                elif isFloat(buffer):
                    add(buffer, "REAL_VAL")
                elif isInt(buffer):
                    add(buffer, "INT_VAL")
                elif isString(buffer):
                    add(buffer, "STRING_VAL")
                else:
                    add(buffer, "ERRO")

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
        if isPalavraReservada(buffer):
            add(buffer, palavras_reservadas[buffer])
        elif isFunc(buffer):
            add(buffer, "FUNC")
        elif isClass(buffer):
            add(buffer, "CLASSE")
        elif isIdent(buffer):
            add(buffer, "IDENT")
        elif isFloat(buffer):
            add(buffer, "REAL_VAL")
        elif isInt(buffer):
            add(buffer, "INT_VAL")
        elif isComentario(buffer):
            add(buffer, "COMENTARIO")
        elif isString(buffer):
            add(buffer, "STRING_VAL")
        else:
            add(buffer, "ERRO")

    if comentario_current:
        print("Erro léxico: comentário não fechado (faltando $ no final).")
        add(buffer, "ERRO")

    display()

main()
