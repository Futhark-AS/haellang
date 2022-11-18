import ply.lex as lex
import re

reserved = {
'plussær':'PLUS',
'minusær':'MINUS',
'gangær':'TIMES',
'delær':'DIVIDE',
'ære-samma-som':'EQUALS',
'hællæ':'LPAREN',
'prekæs':'RPAREN',
'småære-enn':'LT',
'mere-enn':'GT',
'ære-samme-som':'EQ',
'dersom-atter':'IF',
'så':'THEN',
'ellers-så':'ELSE',
'åsså-æru-ferdig':'END_OF_IF_THEN_ELSE',
'så-lenge':'WHILE',
'ta-åsså-gjør':'DO',
'ellers-så':'END_OF_WHILE',
'spøtt-ut':'PRINT',
'ente-gjør-no':'PASS',
}

tokens = [ 
    'NAME','NUMBER',
    'END_OF_STATEMENT',
    'ID',
] + list(reserved.values())

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
    x plussær 4.
'''

lexer.input(data1)
for tok in lexer:
    print(tok)