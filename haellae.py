import sys, os, pprint
from parser.parser import parse
from interpreter.interpreter import interpret

hyphenMap = {
    'ære samma som': 'ære-samma-som',
    'dersom atter': 'dersom-atter',
    'spøtt ut': 'spøtt-ut',
    'mere enn': 'mere-enn',
    'åsså æru ferdig': 'åsså-æru-ferdig',
    'ente gjør no': 'ente-gjør-no',
    'mådda med': 'mådda-med',
    'småære enn': 'småære-enn',
    'er prikk lik': 'er-prikk-lik',
    'ta åsså gjør': 'ta-åsså-gjør',
    'åsså gjøru det igjen': 'åsså-gjøru-det-igjen',
    'klart det': 'klart-det',
    'ente rekti': 'ente-rekti',
    'gi dæ':'gi-dæ'
}

def addHyphens(script, hyphenMap):
    for key, value in hyphenMap.items():
        script = script.replace(key, value)
    print(script)
    return script

def main(args):
    if(len(args) == 0):
        raise FileNotFoundError("Must provide a path to a file")
    filename = args[0]
    if(not os.path.exists(filename)):
        raise FileNotFoundError("Invalid path or file does not exist")
    script = open(filename).read()
    script = addHyphens(script, hyphenMap)
    parsed_script = parse(script)
    if(parsed_script == None):
        raise SyntaxError("Invalid input")
    interpret(parsed_script)
    


if __name__ == "__main__":
   main(sys.argv[1:])
