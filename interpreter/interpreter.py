import operator
import pprint

statement_return_codes = set(
    'BREAK',
)

def interpret(ast):
    """ Executes an abstract syntax tree

    Args:
        ast (_type_): The abstract syntax tree to be executed 
    """

    # pprint.pprint(ast)
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
                
            case 'assign-function':
                parameter_list = interpret_internal(ast[2], None)
                assignment_store[ast[1]] = {
                    'parameter_list': parameter_list,
                    'body': ast[3],
                    'return_expression': ast[4]
                }

            case 'run-function': # Run function without return
                function = assignment_store[ast[1]]
                local_dict = dict()
                argument_list = interpret_internal(ast[2], None)
                for key, value in zip(function['parameter_list'], argument_list):
                    local_dict[key] = value

                interpret_internal(function['body'], dict(assignment_store , **local_dict))

            case 'parameters':
                if len(ast) == 3:
                    return [ast[1]] + interpret_internal(ast[2], assignment_store)
                return [ast[1]]

            
            case 'expression-statement':
                interpret_internal(ast[1], assignment_store)
            case 'if-statement':
                if interpret_internal(ast[1], assignment_store):
                    return interpret_internal(ast[2], assignment_store)
                return interpret_internal(ast[3], assignment_store)
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
                    case 'MOD':
                        op = operator.mod
                    case _ : 
                        raise('Illegal binary expression type')
                return op(interpret_internal(ast[2], assignment_store), interpret_internal(ast[3], assignment_store))
            case 'group-expression':
                return interpret_internal(ast[1], assignment_store)
            case 'literal-expression':
                return ast[1]
            case 'variable-expression':
                return assignment_store[ast[1]]
            case 'list-expression':
                return interpret_internal(ast[1], assignment_store)
            case 'list-body':
                if len(ast) == 3:
                    return [interpret_internal(ast[1], assignment_store)] + interpret_internal(ast[2], assignment_store)
                return [interpret_internal(ast[1], assignment_store)]
            case 'print-function':
                print(interpret_internal(ast[1], assignment_store))
            case 'push-function':
                list_ref = interpret_internal(ast[2], assignment_store)
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke legge te i noe som ente er e bråtæ'))
                list_ref.append(interpret_internal(ast[1], assignment_store))
            case 'pop-function':
                list_ref = interpret_internal(ast[1], assignment_store)
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke græbbe ifra noe som ente er e bråtæ'))
                return list_ref.pop()
            case 'index-expression':
                index = interpret_internal(ast[1], assignment_store)
                list_ref = interpret_internal(ast[2], assignment_store)
                if not type(index) == int:
                    raise(TypeError('Du kanke titte på en plass som ente er et tall uten kåmma'))
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke utifra noe som ente er e bråtæ'))
                if index < 1 or index > len(list_ref):
                    raise(IndexError(f'Dæven æ mårr! Klaræru ente å telle eller? Ærnte en plass {index} i den bråtæn.'))
                return list_ref[index-1]
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
                raise(ValueError(f'Illegal AST Node {ast[0]}'))

    interpret_internal(ast, assignment_store)
