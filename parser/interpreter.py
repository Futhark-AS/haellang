import operator

statement_return_codes = set(
    'BREAK',
)

def interpret(ast):
    """ Executes an abstract syntax tree

    Args:
        ast (_type_): The abstract syntax tree to be executed 
    """

    # Assignment store to hold the values of all variables
    assignment_store = dict()

    # Stack for functions 
    stack = list()

    def interpret_internal(ast, assignment_store):
        match ast[0]:
            case 'recursive-statement':
                for i in range(2):
                    code = interpret_internal(ast[i+1], assignment_store)
                    match code:
                        case 'BREAK':
                            return 'BREAK'
                        case _:
                            pass
            case 'assign-statement':
                assignment_store[ast[1]] = interpret_internal(ast[2], assignment_store)
            case 'if-statement':
                if (interpret_internal(ast[1], assignment_store)):
                    code = interpret_internal(ast[2], assignment_store)
                else:
                    code = interpret_internal(ast[3], assignment_store)
                match code:
                    case 'BREAK':
                        return 'BREAK'
                    case _:
                        pass
            case 'binary-expression': 
                op = None
                match ast[1]:
                    case 'GT':
                        op = operator.gt
                    case 'LT':
                        op = operator.lt
                    case 'EQ':
                        op = operator.eq
                    case 'PLUS':
                        op = operator.add
                    case 'MINUS':
                        op = operator.sub
                    case 'TIMES':
                        op = operator.mul
                    case 'DIVIDE':
                        op = operator.floordiv
                    case _ : 
                        raise('Illegal binary expression type')
                return op(interpret_internal(ast[2], assignment_store), interpret_internal(ast[3], assignment_store))
            case 'group-expression':
                return interpret_internal(ast[1], assignment_store)
            case 'literal-expression':
                return ast[1]
            case 'variable-expression':
                return assignment_store[ast[1]]
            case 'print-statement':
                print(interpret_internal(ast[1], assignment_store))
            case 'pass-statement':
                pass
            case 'while-statement':
                while interpret_internal(ast[1], assignment_store):
                    code = interpret_internal(ast[2], assignment_store)
                    match code:
                        case 'BREAK':
                            break
                        case _:
                            pass
            case 'break-statement':
                return 'BREAK'
            case _:
                raise('Illegal AST Node')

    interpret_internal(ast, assignment_store)