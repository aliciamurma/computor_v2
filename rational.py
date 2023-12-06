from library import *
from aux import *

def ft_save_rational(var):
    var2 = var.split('=')
    new_var = MyVar(var2[0], var2[1])
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    print(var2[1])
    #print(ft_find_variable(variables, var2[0]))

def ft_is_rational_numer(var):
    print("Inside is rational")
    var2 = var.split('=')
    if len(var2) != 2:
        return (False)
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    if right_side.isdigit():
        return (True)
    return (False)