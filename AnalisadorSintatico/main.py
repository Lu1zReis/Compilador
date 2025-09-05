parse_table = {
    "E": {
        "IDENT": ["T", "E'"],
        "(": ["T", "E'"]
    },
    "E'": {
        "OP_ARITM": ["OP_ARITM", "T", "E'"],
        "OP_ARITM": ["OP_ARITM", "T", "E'"],
        ")": ["ε"],
        "$": ["ε"]
    },
    "T": {
        "IDENT": ["F", "T'"],
        "(": ["F", "T'"]
    },
    "T'": {
        "OP_ARITM": ["OP_ARITM", "F", "T'"],
        "OP_ARITM": ["OP_ARITM", "F", "T'"],
        "OP_ARITM": ["ε"],
        "OP_ARITM": ["ε"],
        ")": ["ε"],
        "$": ["ε"]
    },
    "F": {
        "IDENT": ["IDENT"],
        "(": ["(", "E", ")"]
    }
}


def carregar_tokens(caminho_arquivo):
    tokens = []
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("<") and "," in linha:
                tipo = linha.split(",")[0].strip("<>").strip()
                lexema = linha.split(",")[1].strip(" >")
                
                if tipo == "TOKEN":  
                    continue  # ignora cabeçalho
                elif tipo == "EOF":
                    tokens.append(("$", "$"))  # adiciona símbolo de fim de entrada
                else:
                    tokens.append((tipo, lexema))
    return tokens


def parser_ll1(tokens, parse_table, start_symbol="E"):
    stack = ["$", start_symbol]
    input_tokens = [tok for tok, lex in tokens]  # só pega os tipos
    cursor = 0

    print("Tokens de entrada:", input_tokens)

    while stack:
        top = stack.pop()
        current = input_tokens[cursor]

        if top == "ε":
            continue
        elif top == current:  # terminal casa
            print(f"✔ Reconhecido: {current}")
            cursor += 1
        elif top in parse_table:  # não terminal
            if current in parse_table[top]:
                production = parse_table[top][current]
                print(f"{top} → {' '.join(production)}")
                for symbol in reversed(production):
                    stack.append(symbol)
            else:
                raise SyntaxError(f"Erro: não há produção para {top} com lookahead {current}")
        else:
            raise SyntaxError(f"Erro: esperado {top}, encontrado {current}")

        if top == "$" and current == "$":
            print("✅ Análise concluída com sucesso!")
            return True

    return False


if __name__ == "__main__":
    tokens = carregar_tokens("tokens_saida.txt")  # arquivo com os <TOKEN, LEXEMA>
    parser_ll1(tokens, parse_table)
