import sys
sys.path.append("..")

from parser.parser import parse
from interpreter.interpreter import interpret
from haellae import execute
import filecmp

class t_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    ENDITALIC = '\x1B[0m'

tests = [
    'assignment_test',
    'while_test',
    'operators_test',
    'if_else_statement_test',
    'while_with_break_test',
    'list_test',
    'list_operations_test',
]

def run_tests():
    for test in tests:
        stdout = sys.stdout
        with open(f'temp/{test}_output.txt', 'w') as sys.stdout:
            execute(f'test_data/{test}.haellae')
        sys.stdout = stdout 
        if not filecmp.cmp(f'temp/{test}_output.txt', f'test_data/{test}_c.txt'):
            print(f'{t_colors.FAIL}{t_colors.BOLD}X Test: {t_colors.WARNING}{t_colors.ITALIC}{test}{t_colors.ENDITALIC}{t_colors.FAIL} failed with incorrect output{t_colors.ENDC}')
        else:
            print(f'{t_colors.OKGREEN}{t_colors.BOLD}✓ Test: {t_colors.OKCYAN}{t_colors.ITALIC}{test}{t_colors.ENDITALIC}{t_colors.OKGREEN} completed successfully{t_colors.ENDC}')


    


def main():
    run_tests()

if __name__ == '__main__':
    main()