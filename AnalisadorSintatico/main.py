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

                # ignorando o cabeçalho
                if tipo == "TOKEN":  
                    continue  
                elif tipo == "EOF":
                    # adicionando símbolo de fim de entrada
                    tokens.append(("$", "$"))  
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

        # terminal casa
        elif top == current:  
            print(f"Reconhecido: {current}")
            cursor += 1

        # não terminal
        elif top in parse_table:
            if current in parse_table[top]:
                production = parse_table[top][current]
                print(f"{top} -> {' '.join(production)}")
                for symbol in reversed(production):
                    stack.append(symbol)
            else:
                expected = list(parse_table[top].keys())
                raise SyntaxError(
                    f"Erro de sintaxe: para '{top}', esperado {expected}, mas encontrou '{current}'"
                )

        else:
            raise SyntaxError(f"Erro: esperado {top}, encontrado {current}")

        if top == "$" and current == "$":
            print("Análise concluída com sucesso!")
            return True

    return False


if __name__ == "__main__":
    tokens = carregar_tokens("tokens_saida.txt")  # arquivo com os <TOKEN, LEXEMA>
    if (parser_ll1(tokens, parse_table)):
        print("A gramática pertence à linguagem.")
    else:
        print("A gramática não pertence à linguagem.")
