import operator
import sys
import pprint
import importlib
from dataclasses import dataclass
from enum import Enum

class Signal(Enum):
    """
    Emum for all possible signals that interrupt normal 
    program flow
    """
    NONE = 0
    BREAK = 1
    RETURN = 2

@dataclass
class ExecutionState:
    """
    Represents the current execution state of the program
    """
    signal: Signal = Signal.NONE
    assignment: str = ''

def interpret(ast, assignment_store = None):
    """ Executes an abstract syntax tree

    Args:
        ast (_type_): The abstract syntax tree to be executed 
    """
    sys.tracebacklimit = 10

    # Assignment store to hold the values of all variables
    if not assignment_store:
        assignment_store = dict()

    execution_state = ExecutionState()

    def interpret_internal(ast, assignment_store : dict, execution_state: ExecutionState):
        match ast[0]:
            case 'recursive-statement':
                val1 = interpret_internal(ast[1], assignment_store, execution_state)
                if execution_state.signal != Signal.NONE:
                    return val1
                val2 = interpret_internal(ast[2], assignment_store, execution_state)
                return val2 if val2!=None else val1
                            
            case 'assign-statement':
                execution_state.assignment = ast[1]
                assignment_store[ast[1]] = interpret_internal(ast[2], assignment_store, execution_state)
                
            case 'function-expression':
                if len(ast)==3:
                    parameter_list = interpret_internal(ast[1], assignment_store, execution_state)
                    function_body = ast[2]
                else:
                    parameter_list = []
                    function_body = ast[1]
                return function(parameter_list, assignment_store, function_body, execution_state)

            case 'function-application-expression': # Run function and return
                if len(ast) == 3:
                    args = interpret_internal(ast[2], assignment_store, execution_state)
                else:
                    args = []
                f = assignment_store[ast[1]]
                return f(args)
            
            case 'function-import-application-expression': # Run function and return
                if len(ast) == 4:
                    args = interpret_internal(ast[3], assignment_store, execution_state)
                else:
                    args = []
                method = getattr(assignment_store[ast[1]], ast[2])
                return method(*args)

            case 'parameters':
                if len(ast) == 3:
                    return [ast[1]] + interpret_internal(ast[2], assignment_store, execution_state)
                return [ast[1]]
            
            case 'import-statement':
                import_name = ast[2]
                module_name = ast[1]
                module = importlib.import_module(module_name)
                assignment_store[import_name] = module

            case 'expression-statement':
                return interpret_internal(ast[1], assignment_store, execution_state)
                
            case 'if-statement':
                if interpret_internal(ast[1], assignment_store, execution_state):
                    return interpret_internal(ast[2], assignment_store, execution_state)
                return interpret_internal(ast[3], assignment_store, execution_state)
            
            case 'binary-expression': 
                ast2_interpreted = interpret_internal(ast[2], assignment_store, execution_state)
                ast3_interpreted = interpret_internal(ast[3], assignment_store, execution_state)
                op = None
                match ast[1]:
                    case 'GT':
                        op = operator.gt
                    case 'LT':
                        op = operator.lt
                    case 'EQ':
                        op = operator.eq
                    case 'PLUS':
                        if(type(ast2_interpreted) == str and type(ast3_interpreted) == str):
                            op = operator.concat
                        else:
                            op = operator.add
                    case 'MINUS':
                        op = operator.sub
                    case 'TIMES':
                        op = operator.mul
                    case 'DIVIDE':
                        op = operator.truediv
                    case 'MOD':
                        op = operator.mod
                    case _ : 
                        raise('Illegal binary expression type')
                return op(ast2_interpreted, ast3_interpreted)
            
            case 'group-expression':
                return interpret_internal(ast[1], assignment_store, execution_state)
            
            case 'literal-expression':
                return ast[1]
            
            case 'variable-expression':
                return assignment_store[ast[1]]
            
            case 'list-expression':
                if len(ast) ==2 :
                    return interpret_internal(ast[1], assignment_store, execution_state)
                return list()
            
            case 'list-body':
                if len(ast) == 3:
                    return [interpret_internal(ast[1], assignment_store, execution_state)] + interpret_internal(ast[2], assignment_store, execution_state)
                return [interpret_internal(ast[1], assignment_store, execution_state)]
            
            case 'dict-expression':
                if len(ast) == 2:
                    return interpret_internal(ast[1], assignment_store, execution_state)
                return dict()
            
            case 'dict-body':
                if len(ast) == 4:
                    tail_dict = interpret_internal(ast[1], assignment_store, execution_state)
                    key = interpret_internal(ast[2], assignment_store, execution_state)
                    value = interpret_internal(ast[3], assignment_store, execution_state)
                    tail_dict[key] = value
                    return tail_dict
                key = interpret_internal(ast[1], assignment_store, execution_state)
                value = interpret_internal(ast[2], assignment_store, execution_state)
                return {key:value}

            case 'print-function':
                print(interpret_internal(ast[1], assignment_store, execution_state))
                
            case 'print-without-newline-function':
                print(interpret_internal(ast[1], assignment_store, execution_state), end='')
                
            case 'push-function':
                list_ref = interpret_internal(ast[2], assignment_store, execution_state)
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke legge te i noe som ente er e bråtæ'))
                list_ref.append(interpret_internal(ast[1], assignment_store, execution_state))
                
            case 'pop-function':
                list_ref = interpret_internal(ast[1], assignment_store, execution_state)
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke græbbe ifra noe som ente er e bråtæ'))
                return list_ref.pop()
            
            case 'index-expression':
                index = interpret_internal(ast[1], assignment_store, execution_state)
                list_ref = interpret_internal(ast[2], assignment_store, execution_state)
                if not type(index) == int:
                    raise(TypeError(f'Du kanke titte på en plass som ente er et tall uten kåmma. Du putta inn {type(index)}'))
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke ta utifra noe som ente er e bråtæ'))
                if index < 1 or index > len(list_ref):
                    raise(IndexError(f'Dæven æ mårr! Klaræru ente å telle eller? Ærnte en plass {index} bråtæn ({list_ref}).'))
                return list_ref[index-1]
            
            case 'change-index-expression':
                list_ref = interpret_internal(ast[2], assignment_store, execution_state)
                index = interpret_internal(ast[1], assignment_store, execution_state)
                value = interpret_internal(ast[3], assignment_store, execution_state)
                if not type(index) == int:
                    raise(TypeError(f'Du kanke titte på en plass som ente er et tall uten kåmma. Du putta inn {type(index)}'))
                if not type(list_ref) == list:
                    raise(TypeError('Du kanke ta utifra noe som ente er e bråtæ'))
                if index < 1 or index > len(list_ref):
                    raise(IndexError(f'Dæven æ mårr! Klaræru ente å telle eller? Ærnte en plass {index} bråtæn ({list_ref}).'))
                list_ref[index - 1] = value
                
            case 'lookup-expression':
                dict_ref = interpret_internal(ast[2], assignment_store, execution_state)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke slå opp i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store, execution_state)
                if not is_hashable(key):
                    raise(TypeError(f'Du kanke slå opp på noe som ente er hasjbart ({type(key)==str})'))
                return dict_ref[key]
            
            case 'add-expression':
                dict_ref = interpret_internal(ast[3], assignment_store, execution_state)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke legge te ett oppslag i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store, execution_state)
                if not is_hashable(key):
                    raise(TypeError('Du kanke legge te noe som ente er hasjbart'))
                dict_ref[key] = interpret_internal(ast[2], assignment_store, execution_state)
                
            case 'remove-expression':
                dict_ref = interpret_internal(ast[2], assignment_store, execution_state)
                if not type(dict_ref) == dict:
                    raise(TypeError('Du kanke fjærne ett oppslag i noe som ente er e orlbok'))
                key = interpret_internal(ast[1], assignment_store, execution_state)
                if not is_hashable(key):
                    raise(TypeError('Du kanke fjærne noe som ente er hasjbart'))
                del dict_ref[key] 
                
            case 'length-function':
                ref = interpret_internal(ast[1], assignment_store, execution_state)
                if not type(ref) == list and not type(ref) == str:
                    raise(TypeError('Du kanke finne lengden på noe som ente er e bråtæ eller e streng. Du prøvde type: ' + str(type(ref))))
                return len(ref)
            
            case 'pass-statement':
                pass
            
            case 'while-statement':
                while interpret_internal(ast[1], assignment_store, execution_state):
                    value = interpret_internal(ast[2], assignment_store, execution_state)
                    if execution_state.signal == Signal.RETURN:
                        return value
                    if execution_state.signal == Signal.BREAK:
                        execution_state.signal = Signal.NONE
                        return 
                            
            case 'break-statement':
                execution_state.signal = Signal.BREAK
            
            case 'return-statement':
                execution_state.signal = Signal.RETURN
                return interpret_internal(ast[1], assignment_store, execution_state)

            case 'empty':
                return 
            
            case _:
                raise(ValueError(f'Illegal AST Node {ast[0]}'))

    def function(params, assignment_store : dict, statement, execution_state : ExecutionState):
        environment = assignment_store.copy()
        name = execution_state.assignment
        def runnable_function(args):
            for (param, arg) in zip(params, args):
                environment[param] = arg
            if name:
                environment[name] = runnable_function
            return  interpret_internal(statement, environment.copy(), ExecutionState())
        return runnable_function

    value = interpret_internal(ast, assignment_store, execution_state)
    return (value, assignment_store)


def is_hashable(obj):
    return any(map(lambda t: type(obj)==t, [int, float, str, tuple]))
