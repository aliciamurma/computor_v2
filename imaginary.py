from library import *
from aux import *
import re

def ft_save_imaginary(left, right):
    print("Save imaginary")
    right = ft_separate_i(right)
    replaced = ft_replace_variables(right)
    new_var = MyVar(left, replaced)
    variables[left] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, left)
    print(value.value)

def ft_separate_i(var):
    # Definir una expresión regular para buscar los símbolos como separadores
    pattern = r'\b\w+\b|[()+\-^*/%]|i'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str

# \s* permite cero o más espacios en blanco antes del signo 
# [+-]? permite un signo opcional
# \d+ busca uno o más dígitos
def ft_get_i(var):
    patron = re.compile(r'\s*([+-]?\s*\d+)\s*i') # Encuentra +- y despues un termino
    coincidences = patron.search(var) # Buscar coincidencias en var

    if coincidences:
        value = coincidences.group(1)
        return value
    else:
        return 0

# (?![\w\s]*i) indica que no tiene que estar seguido de la letra 'i
def ft_get_nbr(var):
    patron = re.compile(r'\s*([+-]?\s*\d+)(?![\w\s]*i)')
    
    coincidences = patron.search(var) # Buscar coincidencias en var

    if coincidences:
        value = coincidences.group(1)
        return value
    else:
        return 0

def ft_is_imaginary(left, right):
    right = right.replace("*i", "i")
    right = right.replace("* i", "i")
    separated = ft_separate_i(right)
    all_i = ft_get_i(separated)
    all_nbr = ft_get_nbr(separated)
    if all_i != 0: #and all_nbr != 0
        return True
    return False
