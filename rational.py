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
    if (len(left) == 7 and left[:3] == "fun" and left[4] == "(" and left[6] == ")" and left[5].isalpha() and left[3].isalpha()):
        return False
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
