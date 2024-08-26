from library import *

def ft_find_variable(dictionary, name):
    for value in dictionary.values():
        if value is not None and value.name == name:
            return value
    return None

def ft_replace_variables(var):
    print("Before replace:", var)
    parts = var.split(' ')
    if len(parts) == 0:
        print("WTF?????")
        return

    new = []
    for part in parts:
        part = part.strip()
        if part in variables:
            new.append(str(variables[part].value))
        else:
            new.append(part)
    result = ' '.join(new)
    print("the replaced is: ", result)
    return result

def ft_have_function(var):
    if "fun" in var:
        return True
    return False

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

def ft_is_symbol(c):
    if c == '?' or c == '+' or c == '-' or c == '%' or c == '/' or c == '^' or c == '*' or c == '(' or c == ')' or c == '[' or c == ']' or c == ',' or c == '.' or c == ';':
        return True
    return False

def ft_isoperator(spaces):
    for element in spaces:
        if ft_is_multi(element) is True or ft_is_div(element) is True or ft_is_residual(element) is True or ft_is_substraction(element) is True or ft_is_sum(element) is True:
            return True  
    return False

def ft_is_parenthesis_close(spaces):
    for element in spaces:
            if ')' in element:
                return True  
    return False

def ft_not_alphadigit(part1):
    for char in part1:
        if char.isdigit() is True or char.isalpha() is True or part1 == '?':
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