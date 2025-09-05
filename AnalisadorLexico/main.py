from os import listdir

# definicoes
delimitadores = [",", ";", "(", ")", "{", "}", '[', ']', '.', '@', '#']
operadores_logic = ["&", "|", "!"]
operadores_aritm = ["+", "-", "*", "/", "%"]
operadores_relac = ["=", ">", "<"]

#dicionario para as palavras reservadas
palavras_reservadas = {
    "func": "FUNC",
    "int": "INT",
    "real": "REAL",
    "string": "STRING",
    "Colecao": "COLECAO",
    "escreva": "ESCREVA",
    "ler": "LEITURA",
    "se": "SE",
    "podeser": "PODESER",
    "senao": "SENAO",
    "para": "PARA",
    "em": "EM",
    "de": "DE",
    "ate": "ATE",
    "enquanto": "ENQUANTO",
    "faca": "FACA",
    "retorno": "RETORNO",
    "jurou": "JUROU",
    "certin": "CERTIN",
    "const": "CONST",
    "Classe": "CLASSE",
    "este": "ESTE",
    "publico": "MODIFICADOR",
    "privado": "MODIFICADOR"
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

def isIdent(buffer):
    if buffer[0].isalpha() and len(buffer) <= 12:
        return all(c.isalpha() or c.isdigit() or c == '_' for c in buffer[1:])
    return False

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
    
    # Abre (ou cria) o arquivo de saída
    with open("../AnalisadorSintatico/tokens_saida.txt", "w", encoding="utf-8") as f:
        f.write("<TOKEN, LEXEMA>\n")
        
        for token, lexema in resultado:
            linha = f"<{token}, {lexema}>\n"
            print(linha.strip())  # imprime no console
            f.write(linha)        # grava no arquivo

        f.write("<EOF, $>\n")


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
    if isPalavraReservada(buffer):
        add(buffer, palavras_reservadas[buffer])
    elif isIdent(buffer):
        add(buffer, "IDENT")  
    elif isFloat(buffer):
        add(buffer, "REAL")
    elif isInt(buffer):
        add(buffer, "INT")
    elif isString(buffer):
        add(buffer, "STRING")
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

def escolheArquivo():
    exemplos = []
    for i, arquivo in enumerate(listdir("exemplos")):
        exemplos.append(arquivo)
        print(f"{i} - {arquivo}")
    escolha = int(input("Dejesa ver qual saída de exemplo? "))
    
    return exemplos[escolha]


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

                
            if (isEnd(carac) and not comentario_current) or (carac_unico_especial and (not string_current) and not comentario_current):
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

escolha = escolheArquivo()
main(f"exemplos/{escolha}")
