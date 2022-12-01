import sys, os, io
from parser.parser import parse
from interpreter.interpreter import interpret
import pathlib

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(f"{__location__}/stl/haellae.haellae", "r") as f:
    standard_library = f.read()

def execute(filename):
    script = io.open(filename, mode="r", encoding="utf-8").read()
    script = standard_library + script
    parsed_script = parse(script)
    if(parsed_script == None):
        raise SyntaxError("Invalid input")
    interpret(parsed_script)
    

def main(args):
    if(len(args) == 0):
        raise FileNotFoundError("Must provide a path to a file")
    filename = args[0]
    if(not os.path.exists(filename)):
        raise FileNotFoundError("Invalid path or file does not exist")
    execute(filename)


if __name__ == "__main__":
   main(sys.argv[1:])
