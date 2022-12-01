import sys, os, io
from parser.parser import parse
from interpreter.interpreter import interpret

def repl():
    assignment_store = dict()
    while True:
        statement = input('$ ')
        ast = parse(statement)
        value, assignment_store = interpret(ast, assignment_store)
        print(f'- {value}')
        