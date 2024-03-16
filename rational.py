from library import *
from aux import *

def ft_save_rational(left, right):
    replaced = ft_replace_variables(right)
    new_var = MyVar(left, replaced)
    variables[left] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, left)
    print(value.value)

def ft_is_rational_number(left, right):
    print("Inside is rational")
    replaced = ft_replace_variables(right)
    try:
        int(replaced)
        return (True)
    except ValueError:
        try:
            float(replaced)
            return (True)
        except ValueError:
            return (False)
    return (False)
