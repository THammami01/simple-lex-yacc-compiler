from types import resolve_bases
import ply.yacc as yacc
from mylexer import tokens


def p_expression_num(p):
    "expression : NUMBER"
    p[0] = p[1]
    print(p[0], p[1])


def p_expression_add(p):
    "expression : expression OPADD expression"
    if(p[2] == "+"):
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]
    print(p[0], p[1], p[2], p[3])


def p_expression_mul(p):
    "expression : expression OPMUL expression"
    if(p[2] == "*"):
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]
    print(p[0], p[1], p[2], p[3])


def p_error(p):
    print("Syntax error in input!")


precedence = (
    ('left', 'OPADD'),
    ('left', 'OPMUL'),
)

myparser = yacc.yacc()

data = '''2 + 1 * 2
'''

result = myparser.parse(data)
print(result)
