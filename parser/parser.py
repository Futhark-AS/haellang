import ply.lex as lex
import ply.yacc as yacc
import re
import sys 

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
    'en-bråtæ-beståænes-av':'START_OF_LIST',
    'å':'LIST_ITEM_SEPARATOR',
    'å-det-var-det':'END_OF_LIST',
    'legg-te':'PUSH',
    'i-bråtæn':'IN_LIST',
    'græbb-fra':'POP',
    'plass-nummer':'ARRAY_INDEX',
    'en-fungsjon':'FUNCTION',
    'såm-brukær' : 'WITH_PARAMS',    
    'såm-gjør': 'START_OF_FUNCTION',
    'åså-varn-færi' : 'END_OF_FUNCTION',
    'kjør':'RUN',
    'med':'WITH',
    'gi-tilbake':'RETURN',
    'kåmma':'COMMA',
    'e-orlbok-beståænes-av':'START_OF_DICT',
    'å-så-var-orlboka-færi':'END_OF_DICT',
    'betyænes':'DICT_PAIR_SEPARATOR',
    'slå-opp':'DICT_LOOKUP',
    'i-orlboka':'IN_DICT',
    'størlsen-a':'LENGTH',
    'fjærn':'DICT_REMOVE',
}

tokens = [ 
    'NAME','NUMBER', 'STRING', 
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

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    raise(ValueError(f'Ulovli bokstav {t.value[0]}'))

t_ignore = ' \t'

lexer = lex.lex(reflags=re.UNICODE|re.VERBOSE)

precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'COMMA'),
    ('nonassoc', 'IN_DICT', 'IN_LIST'),
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

def p_expression_float(p):
    '''expression : NUMBER COMMA NUMBER'''
    p[0] = ('literal-expression',float(str(p[1])+'.'+str(p[3])))

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('literal-expression', p[1])
    
def p_expression_dict_empty(p):
    '''expression : START_OF_DICT END_OF_DICT'''
    p[0] = ('dict-expression',)
    
def p_expression_dict(p):
    '''expression : START_OF_DICT dict-body END_OF_DICT'''
    p[0] = ('dict-expression', p[2])
    
def p_expression_dict_body_recursive(p):
    '''dict-body : dict-body  LIST_ITEM_SEPARATOR expression DICT_PAIR_SEPARATOR expression'''
    p[0] = ('dict-body', p[1], p[3], p[5])

def p_expression_dict_body_base(p):
    '''dict-body : expression DICT_PAIR_SEPARATOR expression'''
    p[0] = ('dict-body', p[1], p[3])
    
def p_expression_list_empty(p):
    '''expression : START_OF_LIST END_OF_LIST'''
    p[0] = ('list-expression',)

def p_expression_list(p):
    '''expression : START_OF_LIST list-body END_OF_LIST'''
    p[0] = ('list-expression', p[2])

def p_expression_list_body_recursive(p):
    '''list-body : expression LIST_ITEM_SEPARATOR list-body'''
    p[0] = ('list-body', p[1], p[3])

def p_expression_list_body_base(p):
    '''list-body : expression'''
    p[0] = ('list-body', p[1])
    
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

def p_statement_expression(p):
    'statement : expression END_OF_STATEMENT'
    p[0] = ('expression-statement', p[1])

def p_statement_if(p):
    'statement : IF expression THEN statement ELSE THEN statement END_OF_IF_THEN_ELSE END_OF_STATEMENT'
    p[0] = ('if-statement', p[2], p[4], p[7])

def p_variable_parameters(p):
    'parameters : NAME LIST_ITEM_SEPARATOR parameters'
    p[0] = ('parameters', p[1], p[3])

def p_variable_parameters_base(p):
    '''parameters : NAME
                  | empty'''
    p[0] = ('parameters', p[1])

def p_empty(p):
    'empty :'
    p[0] = None

'''
----------------- functions start ----------------- bare for oversikt
'''
def p_function_expression(p):
    'expression : FUNCTION WITH_PARAMS parameters START_OF_FUNCTION statement END_OF_FUNCTION'
    p[0] = ('function-expression', p[3], p[5])

def p_function_expression_no_params(p):
    'expression : FUNCTION START_OF_FUNCTION statement END_OF_FUNCTION'
    p[0] = ('function-expression', p[3])

def p_function_application(p):
    'expression : RUN NAME WITH_PARAMS list-body END_OF_STATEMENT'
    p[0] = ('function-application-expression', p[2], p[4])

def p_function_application_no_args(p):
    'expression : RUN NAME END_OF_STATEMENT'
    p[0] = ('function-application-expression', p[2])

def p_return_statement(p):
    'statement : RETURN expression'
    p[0] = ('return-expression', p[2])

'''
----------------- functions end -----------------
'''
def p_statement_assign(p):
    'statement : NAME EQUALS expression END_OF_STATEMENT'
    p[0] = ('assign-statement', p[1], p[3])

def p_statement_break(p):
    'statement : BREAK END_OF_STATEMENT'
    p[0] = ('break-statement',)

def p_statement_while(p):
    'statement : WHILE expression DO statement END_OF_WHILE END_OF_STATEMENT'
    p[0] = ('while-statement', p[2], p[4])
    
def p_expression_print(p):
    'expression : PRINT expression'
    p[0] = ('print-function', p[2])

def p_expression_push(p):
    'expression : PUSH expression IN_LIST expression'
    p[0] = ('push-function', p[2], p[4])

def p_expression_pop(p):
    'expression : POP expression'
    p[0] = ('pop-function', p[2])

def p_expression_array_index(p):
    'expression : ARRAY_INDEX expression IN_LIST expression'
    p[0] = ('index-expression', p[2], p[4])
    
def p_expression_dict_lookup(p):
    'expression : DICT_LOOKUP expression IN_DICT expression'
    p[0] = ('lookup-expression', p[2], p[4])

def p_expression_dict_add(p):
    'expression : PUSH expression DICT_PAIR_SEPARATOR expression IN_DICT expression'
    p[0] = ('add-expression', p[2], p[4], p[6])

def p_expression_dict_remove(p):
    'expression : DICT_REMOVE expression IN_DICT expression'
    p[0] = ('remove-expression', p[2], p[4])
    
def p_expression_length(p):
    'expression : LENGTH expression'
    p[0] = ('length-function', p[2])

def p_statement_pass(p):
    'statement : PASS END_OF_STATEMENT'
    p[0] = ('pass-statement',)
    
def p_error(p):
    if p is not None: 
        raise ValueError(f"\033[91mUnexpected Token '{p.value} on line {p.lineno}'\033[0m") from None
    else:
        raise(ValueError('Unexpected end of input'))
        
# Error rule for syntax errors
# Build the parser
parser = yacc.yacc(start='statement', debug=True)
    # pprint.pprint(out)

def parse(script):
    sys.tracebacklimit = 0
    lexer.lineno = 1
    return parser.parse(script)

# from interpreter import interpret
# interpret(out)
 
# import sys
# import os
# import io
# import pprint

# def main(args):
#     if(len(args) == 0):
#         raise FileNotFoundError("Must provide a path to a file")
#     filename = args[0]
#     if(not os.path.exists(filename)):
#         raise FileNotFoundError("Invalid path or file does not exist")
#     script = io.open(filename, mode="r", encoding="utf-8").read()
#     print((script))
#     parsed_script = parse(script)
#     if(parsed_script == None):
#         raise SyntaxError("Invalid input")
#     parser_output = parse(parsed_script)
#     pprint.pprint(parser_output)
    
    


# if __name__ == "__main__":
#    main(sys.argv[1:])
