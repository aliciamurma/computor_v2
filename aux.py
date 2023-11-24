
def ft_is_variable(var):
    var2 = var.split('=')
    if len(var2) == 2:
        return (True)
    return (False)

def ft_find_variable(dictionary, name):
    for clave, value in dictionary.items():
        if value is not None:  # Check if value is not None before accessing its attributes
            if value.name == name:
                return value  # Retorna la instancia de MyVar si se encuentra el nombre
    return None 


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
    