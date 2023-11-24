import sys
import re
from rational import *
from imaginary import *
from matrix import *
from function import *
from aux import *
from library import *

variables = {}

def ft_check_statement(statement):
    try:
        var2 = statement.split('=')
        if len(var2) != 2:
            print("Error in syntax")
            sys.exit(-1)
    except error as e:
        print("Error\n", e)

def ft_save_variable(var):
    if ft_is_rational_numer(var):
        ft_save_rational(var)
    elif ft_is_imaginary(var):
        ft_save_imaginary(var)
    elif ft_is_matrix(var):
        ft_save_matrix(var)
    else:
        ft_save_function(var)

def ft_process_statement(statement):
    print("Before check")
    ft_check_statement(statement)
    if (ft_is_variable(statement)):
        ft_save_variable(statement)

def ft_start():
    while True:
        prompt = input("Enter a statement: ")
        while not prompt:
            prompt = input("Enter a statement: ")
        ft_process_statement(prompt)

def main(argv):
    try:
        if len(argv) == 1:
            ft_start()
    except error as e:
        print("Error\n", e);
        sys.exit()

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
