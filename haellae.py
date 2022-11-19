import sys, os, pprint
from parser.parser import parse
from interpreter.interpreter import interpret

def main(args):
    if(len(args) == 0):
        raise FileNotFoundError("Must provide a path to a file")
    filename = args[0]
    if(not os.path.exists(filename)):
        raise FileNotFoundError("Invalid path or file does not exist")
    script = open(filename).read()
    parsed_script = parse(script)
    if(parsed_script == None):
        raise SyntaxError("Invalid input")
    interpret(parsed_script)
    


if __name__ == "__main__":
   main(sys.argv[1:])
