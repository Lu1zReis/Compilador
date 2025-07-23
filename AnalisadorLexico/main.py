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

#dicionario para as palavras reservadas
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
    possibilidade1 = buffer.count('"') % 2 == 0 and buffer[0] == '"' and buffer[len(buffer)-1] == '"' 
    possibilidade2 = buffer.count("'") % 2 == 0 and buffer[0] == "'" and buffer[len(buffer)-1] == "'" 

    if possibilidade1:
        if buffer[1:].index('"')+1 < len(buffer)-1:
            possibilidade1 = False
    if possibilidade2:
        if buffer[1:].index("'")+1 < len(buffer)-1:
            possibilidade2 = False

    return possibilidade1 or possibilidade2 

def isFunc(buffer):
    if not (buffer.startswith('#')):
        return False
    nome = buffer[1:]
    return (1 <= len(nome) <= 24 
            and nome[0].isalpha() 
            and all(c.isalnum() or c == '_' for c in nome[1:]))

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

def isString(buffer):
    possibilidade1 = buffer.count('"') % 2 == 0 and buffer[0] == '"' and buffer[len(buffer)-1] == '"' 
    possibilidade2 = buffer.count("'") % 2 == 0 and buffer[0] == "'" and buffer[len(buffer)-1] == "'" 

    if possibilidade1:
        if buffer[1:].index('"')+1 < len(buffer)-1:
            possibilidade1 = False
    if possibilidade2:
        if buffer[1:].index("'")+1 < len(buffer)-1:
            possibilidade2 = False

    return possibilidade1 or possibilidade2 

def isDelim(buffer):
    return buffer in delimitadores

def isOpLogic(buffer):
    return buffer in operadores_logic

def isOpRelac(buffer):
    return buffer in operadores_relac

def isOpAritm(buffer):
    return buffer in operadores_aritm

def isComentario(buffer):
    return buffer.startswith('$') 

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

def processaComentario(carac, buffer, comentario_current):
    if comentario_current:
        if carac == '$' or carac == '\n':
            add(buffer.strip(), "COMENTARIO")
            return "", False  # encerrou o comentário
        else:
            return buffer + carac, True  # continua acumulando
    elif carac == '$':
        return "", True  # começou o comentário
    else:
        return buffer, comentario_current  # segue normal


def verifyToken(buffer):
    if isClass(buffer):
        add(buffer, "CLASSE")
    elif isIdent(buffer):
        add(buffer, "IDENT")  
    elif isFloat(buffer):
        add(buffer, "REAL")
    elif isInt(buffer):
        add(buffer, "INT")
    elif isString(buffer):
        add(buffer, "STRING")
    elif isFunc(buffer):
        add(buffer, "FUNC")
    elif isComentario(buffer):
        add(buffer, "COMENTARIO")
    else:
        add(buffer, "ERRO")
    

def verifyCarac(caract):
    if isDelim(caract):
        add(caract, "DEL")
    elif isOpLogic(caract):
        add(caract, "OP_LOGIC")
    elif isOpRelac(caract):
        add(caract, "OP_RELAC")
    elif isOpAritm(caract):
        add(caract, "OP_ARITM")

#############################################

def main(nome_arquivo):
    codigo = open(nome_arquivo, "r")
    buffer = ""
    comentario_current = False 
    string_current = False
    
    
    for linha in codigo:
        for carac in linha:
            carac_unico_especial = carac in delimitadores or carac in operadores_logic or carac in operadores_relac or carac in operadores_aritm

            
            if carac == '$' or (comentario_current and carac == "\n"):
                comentario_current = not comentario_current
            if comentario_current == False and carac == "'" or carac == '"':
                string_current = not string_current

                
            if (isEnd(carac) and not comentario_current) or (carac_unico_especial and (not string_current)):
                # tentar classificar o buffer antes de limpar
                
                if buffer:
                    verifyToken(buffer)

                    # sempre ira limpar
                    string_current = False
                    buffer = ""

                # sempre ira limpar
                buffer = ""

                # tratando quando é só um caractere
                verifyCarac(carac)
                
            else:
                buffer += carac

    # se restar algo
    if buffer:
        verifyToken(buffer)

        
    display()

main("AnalisadorLexico/exemplo.txt")
