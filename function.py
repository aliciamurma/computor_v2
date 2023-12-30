import re
from library import *
from aux import *
from operations import *

def ft_second_degree(a, b, c):
    discriminating = b**2 - 4*a*c

    if discriminating > 0:
        x1 = (-b + math.sqrt(discriminating)) / (2*a)
        x2 = (-b - math.sqrt(discriminating)) / (2*a)
        return f"Las soluciones de la ecuación son x1 = {x1} y x2 = {x2}"
    elif discriminating == 0:
        x = -b / (2*a)
        return f"La solución de la ecuación es x = {x}"
    else:
        real = -b / (2*a)
        imaginary = math.sqrt(abs(discriminating)) / (2*a)
        solucion1 = f"{real} + {imaginary}i"
        solucion2 = f"{real} - {imaginary}i"
        return f"Las soluciones de la ecuación son complejas: {solucion1} y {solucion2}"

def ft_get_coeficients2(input):
    # Extraer coeficientes usando expresiones regulares
    match = re.match(r"([-+]?\d*)\s*\*\s*x\^2\s*([-+]?\d*)\s*\*\s*x\s*([-+]?\d*)\s*=\s*0", input)
    
    if match:
        a = int(match.group(1)) if match.group(1) else 1
        b = int(match.group(2)) if match.group(2) else 0
        c = int(match.group(3)) if match.group(3) else 0
        return a, b, c
    else:
        raise ValueError("Invalid format")


def ft_one_letter(expression):
    letters = filter(str.isalpha, expression.lower())
    n_letters = set(letters)
    print("NUMBER OF LETTERS: ", n_letters)
    return len(n_letters)

def ft_get_degree(ecuacion):
    matches = re.findall(r"([-+]?\d*)\s*\*\s*x\^(\d+)", ecuacion) # Utiliza expresiones regulares para encontrar términos con exponentes    
    if not matches:
        return 0 # Si no hay términos con exponentes, el grado es 0

    # Encuentra el exponente máximo
    max_exponente = max(int(match[1]) for match in matches)
    return max_exponente

def ft_print_function(var):
    #pattern = r'(\d*\*?x(?:\^\d+)?)|[-+*/%()]'
    #pattern = r'(\d*\*?x(?:\^\d+)?)|[-+\*/%()]|\w+'
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches) # Construir la cadena de salida uniendo los términos encontrados

    print(output_str)

def ft_is_function(var):
    print("Inside function")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    if ft_one_letter(expression) != 1:
        return False
    
    # Find the variable dynamically
    variables = [c for c in expression if c.isalpha()]
    if not variables:
        return False
    
    variable = variables[0]  # Take the first letter found as the variable
    parameters = expression.split(variable)[1].split(":")[0]
    parameters = parameters.strip("()")
    num_parameters = len(parameters.split(","))  # Count the number of parameters
    return num_parameters > 0  # Verificar si hay al menos un parámetro
    return False
    #ft_expression(expression)

def ft_save_function(var):
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    name = parts[0].strip()
    value = parts[1].strip()
    ft_print_function(value)
    new_var = MyVar(name, value)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary