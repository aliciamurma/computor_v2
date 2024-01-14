import sys
import re
from rational import *
from imaginary import *
from matrix import *
from function import *
from aux import *
from library import *
from operations import *
from interrogant import *

variables = {}

def ft_is_symbol(c):
    if c == '?' or c == '+' or c == '-' or c == '%' or c == '/' or c == '^' or c == '*' or c == '(' or c == ')' or c == '[' or c == ']' or c == ',' or c == '.' or c == ';':
        return True
    return False

def ft_grammar(var):
    bracket = 0

    for i in range(len(var)):
        if var[i] == "(":
            bracket += 1
        if var[i] == ")":
            bracket -= 1
    if bracket != 0:
        return False
    for i in range(len(var)):
        if ft_is_symbol(var[i]) is False and var[i].isdigit() is False and var[i].isalpha() is False:
            print("fails in.. ", var[i])
            return False
    return True

def ft_check_statement(statement):
    try:
        var2 = statement.split('=')
        if len(var2) != 2:
            print("Error in syntax 1")
            return (False)
        part1 = var2[0].strip()
        part2 = var2[1].strip()
        if len(part1) == 1 and part1 == "i":
            print("Error in syntax 2")
            return (False)
        if ft_grammar(part1) is False or ft_grammar(part2) is False:
            print("Error in syntax 2")
            return (False)
    except:
        print("Error 2\n")
    return (True)

def ft_save_variable(var):
    var2 = var.split('=')
    if len(var2) != 2:
        print("ERROR!")
        return
    left = var2[0].strip()
    right = var2[1].strip()
    if ft_ask_value(left, right):
        ft_print_asked(left, right)
    elif ft_is_rational_number(left, right):
        ft_save_rational(left, right)
    elif ft_is_imaginary(left, right):
        ft_save_imaginary(left, right)
    elif ft_is_matrix(left, right):
        ft_save_matrix(left, right)
    elif ft_is_function(left, right):
        ft_save_function(left, right)
    else:
        ft_operate(left, right)

def ft_process_statement(statement):
    if ft_check_statement(statement):
        ft_save_variable(statement)
    else:
        print("I don't understand it")

def ft_start():
    try:
        while True:
            prompt = input("Enter a statement: ")
            prompt = prompt.replace(' ','')
            while not prompt:
                prompt = input("Enter a statement: ")
                prompt = prompt.replace(' ','')
            ft_process_statement(prompt)
    except:
        print("I don't think that a calculator can do it...")


def main(argv):
    if len(argv) == 1:
        ft_start()
    else:
        print("Error")
        sys.exit()

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
