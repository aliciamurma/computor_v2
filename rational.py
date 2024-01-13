from library import *
from aux import *

def ft_save_rational(var):
    var2 = var.split('=')
    if len(var2) != 2:
        return (False)
    right = var2[1].strip()
    replaced = ft_replace_variables(right)
    new_var = MyVar(var2[0], replaced)
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, var2[0])
    print(value.value)

def ft_is_rational_number(var):
    print("Inside is rational")
    var2 = var.split('=')
    if len(var2) != 2:
        return (False)
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    replaced = ft_replace_variables(right_side)
    if replaced.isdigit():
        return (True)
    return (False)
