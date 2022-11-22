import operator
import sys
import pprint
import importlib

statement_return_codes = set(
    'BREAK',
)

def interpret(ast):
    """ Executes an abstract syntax tree

    Args:
        ast (_type_): The abstract syntax tree to be executed 
    """
    sys.tracebacklimit = 10

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
                if len(ast) ==2 :
                    return interpret_internal(ast[1], assignment_store)
                return list()
            case 'list-body':
                if len(ast) == 3:
                    return [interpret_internal(ast[1], assignment_store)] + interpret_internal(ast[2], assignment_store)
                return [interpret_internal(ast[1], assignment_store)]
            case 'dict-expression':
                if len(ast) == 2:
                    return interpret_internal(ast[1], assignment_store)
                return dict()
            case 'dict-body':
                if len(ast) == 4:
                    tail_dict = interpret_internal(ast[1], assignment_store)
                    key = interpret_internal(ast[2], assignment_store)
                    value = interpret_internal(ast[3], assignment_store)
                    tail_dict[key] = value
                    return tail_dict
                key = interpret_internal(ast[1], assignment_store)
                value = interpret_internal(ast[2], assignment_store)
                return {key:value}

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
            case 'lookup-expression':
                dict_ref = interpret_internal(ast[2], assignment_store)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke slå opp i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store)
                if not is_hashable(key):
                    raise(TypeError(f'Du kanke slå opp på noe som ente er hasjbart ({type(key)==str})'))
                return dict_ref[key]
            case 'add-expression':
                dict_ref = interpret_internal(ast[3], assignment_store)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke legge te ett oppslag i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store)
                if not is_hashable(key):
                    raise(TypeError('Du kanke legge te noe som ente er hasjbart'))
                dict_ref[key] = interpret_internal(ast[2], assignment_store)
            case 'remove-expression':
                dict_ref = interpret_internal(ast[2], assignment_store)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke fjærne ett oppslag i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store)
                if not is_hashable(key):
                    raise(TypeError('Du kanke fjærne noe som ente er hasjbart'))
                del dict_ref[key] 
            case 'len-function':
                pass
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


def is_hashable(obj):
    return any(map(lambda t: type(obj)==t, [int, float, str, tuple]))