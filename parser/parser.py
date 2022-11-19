import ply.lex as lex
import ply.yacc as yacc
import re
import pprint

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
    'ellers-så':'ELSE',
    'åsså-æru-ferdig':'END_OF_IF_THEN_ELSE',
    'så-lenge':'WHILE',
    'ta-åsså-gjør':'DO',
    'åsså-gjøru-det-igjen':'END_OF_WHILE',
    'spøtt-ut':'PRINT',
    'klart-det':'TRUE',
    'ente-rekti':'FALSE',
    'gi-dæ':'BREAK',
}

#print(reserved)

tokens = [ 
    'NAME','NUMBER',
    'END_OF_STATEMENT',
] + list(set(reserved.values()))

#print(reserved.values())
#print(tokens)

t_END_OF_STATEMENT = r'[.,]'

def t_ID(t):
    r'([a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ_0-9]*-)*[a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NAME(t):
    r'[a-zA-ZæøåÆØÅ_][a-zA-ZæøåÆØÅ0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex(reflags=re.UNICODE|re.VERBOSE)

data1 = '''
    x ære-samma-som 4.
    dersom-atter x mere-enn 2
    så spøtt-ut x, ellers-så
    ente-gjør-no, åsså-æru-ferdig.
'''
data2 = '''
    x ære-samma-som 4.
'''
data3 = '''
    x ære-samma-som 4.
    y ære-samma-som x plussær 5.
'''
data4 = '''
    x ære-samma-som 4.
    y ære-samma-som hællæ 1 plussær x prekæs gangær 2.
    dersom-atter x plussær y mere-enn 11
    så spøtt-ut y, ellers-så
    spøtt-ut x, åsså-æru-ferdig.
'''
data5 = '''
    i ære-samma-som 0.
    så-lenge i småære-enn 10 
    ta-åsså-gjør 
    i ære-samma-som i plussær 1.
    dersom-atter i gangær i mere-enn 20
    så gi-dæ,
    ellers-så ente-gjør-no,
    åsså-æru-ferdig.
    spøtt-ut i. 
    åsså-gjøru-det-igjen.
'''
data6 = '''
    n ære-samma-som 2.
    så-lenge n småære-enn 100 ta-åsså-gjør 
        p ære-samma-som klart-det.
        d ære-samma-som 2.
        så-lenge d småære-enn n delær 2 plussær 1 ta-åsså-gjør 
            dersom-atter 
                hællæ n mådda-med d prekæs er-prikk-lik 0
            så 
                p ære-samma-som ente-rekti.
                gi-dæ.
            ellers-så 
                ente-gjør-no,
            åsså-æru-ferdig.
            d ære-samma-som d plussær 1.
        åsså-gjøru-det-igjen.
        dersom-atter 
            p 
        så 
            spøtt-ut n. 
        ellers-så
            ente-gjør-no.
        åsså-æru-ferdig.
        n ære-samma-som n plussær 1.
    åsså-gjøru-det-igjen.
'''

lexer.input(data6)
for tok in lexer:
    print(tok)

precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    # ('right', 'UMINUS'),            # Unary minus operator
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
    'statement : IF expression THEN statement ELSE statement END_OF_IF_THEN_ELSE END_OF_STATEMENT'
    p[0] = ('if-statement', p[2], p[4], p[6])

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
    print("Syntax Error in Input!")
    
 
# Error rule for syntax errors
    
# Build the parser
parser = yacc.yacc(start='statement')
out = parser.parse(data6)
pprint.pprint(out)

from interpreter import interpret
interpret(out)
 