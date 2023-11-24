from library import *
from aux import *


# 1 ()
# 2 ^
# 3 * / %
# 4 + -
def ft_expression(var):
    spaces = var.split(' ')
    if ft_is_parenthesis_open(spaces):
        ft_operate_parenthesis(spaces)

def ft_save_function(var):
    print("Save function")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    ft_expression(expression)
