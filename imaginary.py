from library import *
from aux import *
import re

def ft_save_imaginary(var):
    print("Save imaginary: ", var)
    var2 = var.split('=')
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    right_side = ft_separate_i(right_side)
    replaced = ft_replace_variables(right_side)
    new_var = MyVar(var2[0], replaced)
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, var2[0])
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

def ft_is_imaginary(var):
    var2 = var.split('=')
    expression = var2[1].strip()
    expression = expression.replace("*i", "i")
    expression = expression.replace("* i", "i")
    separated = ft_separate_i(expression)
    all_i = ft_get_i(separated)
    all_nbr = ft_get_nbr(separated)
    if all_i != 0 and all_nbr != 0:
        return True
    return False

'''
def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    right_side = var[1].strip()  # Elimina espacios en blanco alrededor
    right_side = ft_separate_i(right_side)
    replaced = ft_replace_variables(right_side)
    if replaced.find("i") == -1:
        return False
    parts = re.split(r'[-+]', replaced)
    if len(parts) != 2:
        return False
    if replaced[-1] == 'i':
        real = parts[0].strip()
        imaginary = parts[1].strip()
    else:
        real = parts[1].strip()
        imaginary = parts[0].strip()

    try:
        if (real.replace("-", "").replace("+", "").isdigit() and
            (imaginary.replace("-", "").replace("+", "").isdigit() or
            (imaginary[-1] == 'i') and imaginary[:-1].replace("-", "").replace("+", "").replace("*", "").isdigit())):
            return True
        else:
            return False
    except ValueError:
        print("No me gusta ese imaginario")
        return False

def agrupar_terminos(cadena):
    # Utilizamos expresiones regulares para separar los términos
    terminos = re.findall(r'(-?\d*\.?\d*)?[ij]|\d+|-?\d*\.?\d*', cadena)
    
    # Inicializamos las partes real e imaginaria
    parte_real = 0
    parte_imaginaria = 0

    # Iteramos sobre los términos y sumamos las partes real e imaginaria
    for termino in terminos:
        if 'i' in termino:
            # Si el término contiene 'i', es parte imaginaria
            parte_imaginaria += complex(0, float(termino.replace('i', '')))
        else:
            # Si no contiene 'i', es parte real
            parte_real += float(termino)

    # Formateamos el resultado
    resultado = f"{parte_real} {'+' if parte_imaginaria.imag >= 0 else '-'} {abs(parte_imaginaria.imag)}i"

    return resultado

'''
