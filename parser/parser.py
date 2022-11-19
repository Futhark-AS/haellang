import ply.lex as lex
import ply.yacc as yacc
import re

reserved = {
    'plussær':'PLUS',
    'minusær':'MINUS',
    'gangær':'TIMES',
    'delær':'DIVIDE',
    'mådda-med':'MOD',
    'ære-samma-som':'EQUALS',
    'hællæ':'LPAREN',
    'prekæs':'RPAREN',
    'småære-enn':'LT',
    'mere-enn':'GT',
    'er-prikk-lik':'EQ',
    'dersom-atter':'IF',
    'så':'THEN',
    'ente-gjør-no':'PASS',
    'ellers':'ELSE',
    'åsså-æru-ferdig':'END_OF_IF_THEN_ELSE',
    'imens':'WHILE', 
    'ta-åsså-gjør':'DO',
    'åsså-gjøru-det-igjen':'END_OF_WHILE',
    'spøtt-ut':'PRINT',
    'klart-det':'TRUE',
    'ente-rekti':'FALSE',
    'gi-dæ':'BREAK',
}

tokens = [ 
    'NAME','NUMBER', 'STRING', 'FLOAT',
    'END_OF_STATEMENT',
] + list(set(reserved.values()))

t_END_OF_STATEMENT = r'[.,]'

def t_ID(t):
    r'([a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ_0-9]*-)*[a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NAME(t):
    r'[a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ0-9_]*'
    return t

def t_FLOAT(t):
    r'\d+.\d+'
    print(t)
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex(reflags=re.UNICODE|re.VERBOSE)

precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | expression MOD expression
                | expression GT expression
                | expression LT expression
                | expression EQ expression'''

    p[0] = ('binary-expression',reserved[p[2]],p[1],p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ('group-expression',p[2])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('literal-expression',p[1])

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('literal-expression', p[1])
    
def p_expression_float(p):
    '''expression : FLOAT'''
    p[0] = ('literal-expression', p[1])

def p_expression_true(p):
    '''expression : TRUE'''
    p[0] = ('literal-expression', True)

def p_expression_false(p):
    '''expression : FALSE'''
    p[0] = ('literal-expression', False)
    
def p_expression_variable(p):
    '''expression : NAME'''
    p[0] = ('variable-expression',p[1])

def p_statement_recursive(p):
    'statement : statement statement'
    p[0] = ('recursive-statement', p[1], p[2])

def p_statement_if(p):
    'statement : IF expression THEN statement ELSE THEN statement END_OF_IF_THEN_ELSE END_OF_STATEMENT'
    p[0] = ('if-statement', p[2], p[4], p[7])

def p_statement_assign(p):
    'statement : NAME EQUALS expression END_OF_STATEMENT'
    p[0] = ('assign-statement', p[1], p[3])

def p_statement_break(p):
    'statement : BREAK END_OF_STATEMENT'
    p[0] = ('break-statement',)

def p_statement_while(p):
    'statement : WHILE expression DO statement END_OF_WHILE END_OF_STATEMENT'
    p[0] = ('while-statement', p[2], p[4])
    
def p_statement_print(p):
    'statement : PRINT expression END_OF_STATEMENT'
    p[0] = ('print-statement', p[2])

def p_statement_pass(p):
    'statement : PASS END_OF_STATEMENT'
    p[0] = ('pass-statement',)
    
def p_error(p):
    if p is not None: 
        print(f"\033[91mUnexpected Token '{p.value}'\033[0m")
    else:
        print('Unexpected end of input')
        
# Error rule for syntax errors
# Build the parser
parser = yacc.yacc(start='statement', debug=True)
# pprint.pprint(out)

def parse(script):
    return parser.parse(script)

# from interpreter import interpret
# interpret(out)
 