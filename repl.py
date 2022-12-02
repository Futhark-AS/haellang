from parser.parser import parse
from interpreter.interpreter import interpret

from cmd import Cmd

 
class Prompt(Cmd):

    prompt = '>>> '
    # intro = "Welcome to the haellang repl!"

    def init(self): 
        self.assignment_store = dict()

    def do_exit(self, _):
        exit(0)
    
    def default(self, statement):
        try:
            self.assignment_store = execute_statement(statement, self.assignment_store)
        except Exception as e:
            print(e)
 
 
    do_EOF = do_exit
 
def execute_statement(statement:str, assignment_store:dict):
    ast = parse(statement)
    value, new_assignment_store = interpret(ast, assignment_store)
    print(f'- {value}')
    return new_assignment_store


def repl():
    prompt = Prompt()
    prompt.init()
    while True:
        try:
            prompt.cmdloop()
        except KeyboardInterrupt as k:
            print('\nKeyboardInterrupt')
