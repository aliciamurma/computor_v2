from aux import *
from library import *

def ft_ask_value(var):
    var2 = var.split('=')
    if len(var2) != 2:
        print("Error in syntax 1")
        return (False)
    part = var2[1].strip()
    if len(part) == 1 and part == "?":
        return True
    return False

def ft_print_asked(var):
    var2 = var.split('=')
    replaced = ft_replace_variables(var2[0])
    print(replaced)
