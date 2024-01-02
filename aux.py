from library import *

def ft_find_variable(dictionary, name):
    for value in dictionary.values():
        if value is not None and value.name == name:
            return value
    return None

def ft_replace_variables(var):
    parts = var.split(' ')
    if len(parts) == 0:
        print("WTF?????")
        return

    new = []
    for part in parts:
        if part in variables:
            print(" is: ", variables[part].value)
            new.append(variables[part].value)
        else:
            new.append(part)
    result = ' '.join(new)
    return result


def ft_is_sum(spaces):
    for element in spaces:
            if '+' in element:
                return True  
    return False

def ft_is_substraction(spaces):
    for element in spaces:
            if '-' in element:
                return True  
    return False

def ft_is_residual(spaces):
    for element in spaces:
            if '%' in element:
                return True  
    return False

def ft_is_div(spaces):
    for element in spaces:
            if '/' in element:
                return True  
    return False

def ft_is_multi(spaces):
    for element in spaces:
            if '*' in element:
                return True  
    return False

def ft_is_parenthesis_close(spaces):
    for element in spaces:
            if ')' in element:
                return True  
    return False

def ft_is_parenthesis_open(spaces):
    for element in spaces:
            if '(' in element:
                return True  
    return False

def ft_suma(a, b):
    return a + b

def ft_resta(a, b):
    return a - b

def ft_multiplicacion(a, b):
    return a * b

def ft_division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."