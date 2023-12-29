'''
def ft_find_variable(dictionary, name):
    print("DONT ENTER IN FOR")
    for clave, value in dictionary.items():
        print("IN ONE FOR")
        if value is not None:  # Check if value is not None before accessing its attributes
            if value.name == name:
                print("Finded!!")
                return value  # Retorna la instancia de MyVar si se encuentra el nombre
    return None 


def ft_find_variable(dictionary, name):
    return variables.get(name, None)
'''

def ft_find_variable(dictionary, name):
    for value in dictionary.values():
        if value is not None and value.name == name:
            print("Found!!")
            return value
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