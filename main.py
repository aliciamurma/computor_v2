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

def ft_grammar_par(var):
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
            print("Fails in.. ", var[i])
            return False
    return True

def ft_grammar_cor(var):
    bracket = 0

    for i in range(len(var)):
        if var[i] == "[":
            bracket += 1
        if var[i] == "]":
            bracket -= 1
    if bracket != 0:
        return False
    for i in range(len(var)):
        if ft_is_symbol(var[i]) is False and var[i].isdigit() is False and var[i].isalpha() is False:
            print("Fails in.. ", var[i])
            return False
    return True

def ft_not_alphadigit(part1):
    for char in part1:
        if char.isdigit() is True or char.isalpha() is True or part1 == '?':
            return True
    return False

def ft_isclosed(part2):
    stack = []
    opening = {'(': ')', '[': ']', '{': '}'}
    closing = {')', ']', '}'}

    for char in part2:
        if char in opening:
            stack.append(char)
        if char in closing:
            if not stack or opening[stack.pop()] != char:
                return False
    return True

def ft_excessive_numbers(raw):
    try:
        var = ft_separate_new(raw)
        for i in range(len(var) - 2):
            if var[i].isdigit() == True and var[i + 1] == ' ' and var[i + 2].isdigit() == True:
                return True
        for i in range(len(var) - 2):
            if ft_isoperator(var[i]) == True and var[i + 1] == ' ' and ft_isoperator(var[i + 2]) == True:
                return True
        if ft_isoperator(var[-1]) == True:
            return True
    except:
        return False
    return False

def ft_check_statement(statement):
    try:
        var2 = statement.split('=')
        if len(var2) != 2:
            print("Error in syntax 1, I need one equal")
            return (False)
        part1 = var2[0].strip()
        part2 = var2[1].strip()
        print("PART2 IS:", part2)
        if len(part1) == 0 or len(part2) == 0:
            print("Error in syntax 2, I need something before and after the equal")
            return (False)
        if len(part1) == 1 and part1 == "i":
            print("Error in syntax 3, I cannot save the variable 'i' because it is used for imaginary numbers")
            return (False)
        if ft_grammar_par(part1) is False or ft_grammar_par(part2) is False:
            print("Error in syntax 4, failure in grammar")
            return (False)
        if ft_grammar_cor(part1) is False or ft_grammar_cor(part2) is False:
            print("Error in syntax 4, failure in grammar")
            return (False)
        if part1.isalpha() is False and part1.isdigit() is True:
            print("Error in syntax 5, I am not gonna do nothing without numbers or variables")
            return False
        if ft_not_alphadigit(part1) is False or ft_not_alphadigit(part2) is False:
            print("Error in syntax 6, only special chars")
            return False
        if ft_isclosed(part2) is False or ft_isclosed(part1) is False:
            print("Error in syntax 7, open-close")
            return False
        if part2 != '?':
            if ft_excessive_numbers(part2) is True or ft_excessive_numbers(part1):
                print("Error in syntax 8, stranger things")
                return False
    except:
        print("Error 2\n")
        return False
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
        if ft_is_correct_matrix(left, right):
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
    while True:
        try:
            prompt = input("Enter a statement: ")
            prompt = prompt.replace(' ','')
            while not prompt:
                prompt = input("Enter a statement: ")
                prompt = prompt.replace(' ','')
            ft_process_statement(prompt)
        except:
            print("I don't think that a calculator can do it...")
        if prompt == "EXIT":
            exit()

def main(argv):
    if len(argv) == 1:
        ft_start()
    else:
        print("Error")
        sys.exit()

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
