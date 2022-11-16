import ply.lex as lex

# List of token names. This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_NUMBER(t):  # A regular expression rule with some action code
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):  # Define a rule so we can track line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):  # Error handling rule
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# To use the lexer, you first need to feed it some input text using its input() method.
# After that, repeated calls to token() produce tokens.
# The following code shows how this works:

# Test it out
data = '''3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(f"Line {tok.lineno}: {tok.value} of type {tok.type}")
