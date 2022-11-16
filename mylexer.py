import ply.lex as lex

tokens = (
    "NUMBER",
    "OPADD",
    "OPMUL",
)

t_OPADD = r"[\+-]"
t_OPMUL = r"[\*/]"


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):  # Define a rule so we can track line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):  # Error handling rule
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


mylexer = lex.lex()

if __name__ == "__main__":
    # Test it with some input
    data = '''3 + 4 * 10
    + -20 * 2
    '''

    # Give the lexer the input
    mylexer.input(data)

    # Tokenize
    while True:
        tok = mylexer.token()
        if not tok:
            break  # No more input
        print(f"Line {tok.lineno}: {tok.value} of type {tok.type}")
