# --- Tabela LL(1) com precedência correta (+,-) < (*,/)
parse_table = {
    "E": {
        "IDENT": ["T", "E'"],
        "(": ["T", "E'"]
    },
    "E'": {
        "+": ["+", "T", "E'"],
        "-": ["-", "T", "E'"],
        ")": ["ε"],
        "$": ["ε"]
    },
    "T": {
        "IDENT": ["F", "T'"],
        "(": ["F", "T'"]
    },
    "T'": {
        "*": ["*", "F", "T'"],
        "/": ["/", "F", "T'"],
        "+": ["ε"],
        "-": ["ε"],
        ")": ["ε"],
        "$": ["ε"]
    },
    "F": {
        "IDENT": ["IDENT"],
        "(": ["(", "E", ")"]
    }
}

NONTERMINALS = {"E","E'","T","T'","F"}


def carregar_tokens(caminho_arquivo):
    """
    Lê linhas no formato <TOKEN, LEXEMA> e normaliza para os símbolos
    que a parse_table usa: IDENT, (, ), +, -, *, /, $
    Ignora o cabeçalho <TOKEN, LEXEMA>.
    """
    tokens = []
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or not (linha.startswith("<") and "," in linha):
                continue

            tipo, resto = linha.split(",", 1)
            tipo = tipo.strip("<>").strip()
            lexema = resto.strip(" >").strip()

            # ignorando cabeçalho
            if tipo == "TOKEN":
                continue

            # fim de entrada
            if tipo == "EOF":
                tokens.append(("$", "$"))
                continue

            # mapeando delimitadores para '(' e ')'
            if tipo == "DEL":
                if lexema in ("(", ")"):
                    tokens.append((lexema, lexema))
                else:
                    continue
                continue

            # mapeia operadores aritméticos para + - * /
            if tipo == "OP_ARITM":
                if lexema in {"+", "-", "*", "/"}:
                    tokens.append((lexema, lexema))
                else:
                    # operador fora do escopo desta gramática; ignore/erro
                    continue
                continue

            # identificadores
            if tipo == "IDENT":
                tokens.append(("IDENT", lexema))
                continue

            # qualquer outra coisa é irrelevante para esta gramática
            continue

    return tokens


def parser_ll1(tokens, parse_table, start_symbol="E"):
    stack = ["$", start_symbol]
    input_tokens = [tok for tok, _ in tokens]  # só tipos
    i = 0

    print("Tokens de entrada:", input_tokens)

    while True:
        X = stack[-1]
        a = input_tokens[i] if i < len(input_tokens) else None
        print(f"a=>{a}")
        # log para depurar
        # print(f"Pilha: {stack} | Entrada: {input_tokens[i:]}")

        # aceita
        if X == "$" and a == "$":
            print("Análise concluída com sucesso!")
            return True

        # se topo é não-terminal: consulta tabela
        if X in NONTERMINALS:
            if a in parse_table[X]:
                stack.pop()
                prod = parse_table[X][a]
                print(f"{X} -> {' '.join(prod)}")
                if prod != ["ε"]:
                    stack.extend(reversed(prod))
            else:
                expected = list(parse_table[X].keys())
                raise SyntaxError(
                    f"Erro de sintaxe: para '{X}', esperado {expected}, mas encontrou '{a}'"
                )

        else:
            # se topo é terminal: precisa casar com a entrada
            if X == a:
                stack.pop()
                i += 1
                print(f"Consome '{a}'")
            else:
                raise SyntaxError(f"Erro: esperado '{X}', mas encontrou '{a}'")


if __name__ == "__main__":
    tokens = carregar_tokens("tokens_saida.txt")  
    if parser_ll1(tokens, parse_table):
        print("A cadeia pertence à linguagem.")
    else:
        print("A cadeia NÃO pertence à linguagem.")
