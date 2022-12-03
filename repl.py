from parser.parser import parse
from interpreter.interpreter import interpret

from cmd import Cmd

 
class Prompt(Cmd):

    prompt = '>>> '
    # intro = "Welcome to the haellang repl!"

    def init(self, standard_library): 
        _, self.assignment_store = interpret(parse(standard_library))

    def do_exit(self, _):
        exit(0)
    
    def default(self, statement):
        try:
            self.assignment_store = execute_statement(statement, self.assignment_store)
        except Exception as e:
            print(e.__traceback__)
 
 
    do_EOF = do_exit
 
def execute_statement(statement:str, assignment_store:dict):
    ast = parse(statement)
    value, new_assignment_store = interpret(ast, assignment_store)
    print(f'- {value}')
    return new_assignment_store


def repl(standard_library):
    prompt = Prompt()
    prompt.init(standard_library)
    while True:
        try:
            prompt.cmdloop()
        except KeyboardInterrupt as k:
            print('\nKeyboardInterrupt')
