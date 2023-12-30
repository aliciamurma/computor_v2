import sys
import re
from rational import *
from imaginary import *
from matrix import *
from function import *
from aux import *
from library import *
from operations import *

variables = {}

def ft_check_statement(statement):
    try:
        var2 = statement.split('=')
        if len(var2) != 2:
            print("Error in syntax 1")
            return (False)
    except:
        print("Error 2\n")
    return (True)

def ft_save_variable(var):
    if ft_is_rational_numer(var):
        ft_save_rational(var)
    elif ft_is_imaginary(var):
        ft_save_imaginary(var)
    elif ft_is_matrix(var):
        ft_save_matrix(var)
    elif ft_is_function(var):
        ft_save_function(var)
    else:
        ft_operate(var)

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
