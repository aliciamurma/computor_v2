import re
from aux import *
from library import *
from rational import *
from imaginary import *
from matrix import *
from function import *
from operations import *

def ft_ask_value(left, right):
    part = right.strip()
    if len(part) == 1 and part == "?":
        return True
    return False

def ft_separate(var):
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str

def ft_print_asked(left, right):
    separated = ft_separate(left)
    replaced = ft_replace_variables(separated)
    print("replaced: ", replaced, "right: ", right)
    if ft_is_rational_number(right, replaced):
        print(replaced)
    elif ft_is_imaginary(right, replaced):
        print(replaced)
    elif ft_is_matrix(right, replaced):
        ft_print_matrix(replaced)
    #elif ft_is_function(right, replaced):
    #    print("function!")
    else:
        ft_operate(right, left)