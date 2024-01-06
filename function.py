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

def ft_is_correct_letter(expression, letter):
    letters = ''.join(filter(str.isalpha, expression.lower()))
    n_letters = set(letters)
    if letter in n_letters:
        return True
    return False

def ft_one_letter(expression):
    letters = filter(str.isalpha, expression.lower())
    n_letters = set(letters)
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
    global error
    print("Inside function")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    if not (len(variable) == 7 and variable[:3] == "fun" and variable[4] == "(" and variable[6] == ")" and variable[5].isalpha() and variable[3].isalpha()):
        return False
    if not ft_one_letter(expression):
        error = 1
        return False
    if not ft_is_correct_letter(expression, variable[5]):
        print("its not correct letter")
        error = 1
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

def ft_pre_solve(var):
    var = var.replace("x ^", "x^")
    var = var.replace("* x^", "x^")
    var = var.replace(" x^", "x^")
    var = var.replace("x^ ", "x^")
    var = var.replace("+ ", "+")
    var = var.replace("- ", "-")
    var = var.replace("* ", "*")
    var = var.replace("/ ", "/")
    var = var.replace("% ", "%")
    if var[0].isdigit:
        a = "+"
        var = a + var
    return var

def ft_get_incognita_letter(name):
    return name[5]

def ft_save_function(var):
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    name = parts[0].strip()
    expression = parts[1].strip()

    letter = ft_get_incognita_letter(name)
    separated = ft_separate(expression)
    replaced = ft_replace_variables(separated)
    replaced = ft_pre_solve(replaced)
    print("SEPARED BY CHUNKS IS: ", replaced)
    incog, nbr = ft_separate_x_nbr(replaced)
    degree = ft_get_degree(incog)
    func_dict = ft_get_dictionary(incog, nbr, letter)
    print("Before incog2. ", func_dict)
    saver = ft_get_expression(func_dict)
    # operated = ft_operate_function(replaced)
    name = name[:4] if len(name) >= 4 else name
    new_var = MyVar(name, saver)
    print("name: ", name)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary
    print("check in the dictionary")
    real_value = ft_find_variable(variables, name)
    if real_value:
        print(real_value.value)

def ft_get_expression(incog):
    result = []  # Inicializa como lista vacía
    for key, value in incog.items():
        print("key:", key)
        sign = '+' if value >= 0 else ''  # Determina el signo del valor
        aux = f"{value}x^{key}"  # f-strings para formatear la expresión
        result.append(sign + aux)
    result_str = ' '.join(result)  # Concatena mediante espacios
    return result_str

def ft_get_dictionary(var1, var2, letter):
    incog = {}
    number = [] 

    for i in range(len(var2)):
        number.append(var2[i])
    num_str = ''.join(number)
    incog[0] = eval(num_str)

    print("var1: ", var1)
    for i in range(len(var1)):
        aux = var1[i].split(letter)
        print("AUXX IS: ", aux)
        if aux[0] and len(aux[0]) > 1:
            nbr = int(aux[0].strip())  # Convertir el coeficiente a entero
        else:
            nbr = +1
        if aux[1]:
            degree = int(aux[1].strip().replace("^", "")) 
        else:
            degree = 1
        if degree in incog:
            incog[degree] += nbr
        else:
            incog[degree] = nbr
    return incog

def ft_separate_x_nbr(var):
    incognitas = []
    nbr = []
    var = var.split(' ')

    # Definir una expresión regular para buscar los símbolos como separadores
    for i in range(len(var)):

        if "x" in var[i]:
            aux1 = var[i].strip()
            incognitas.append(aux1)
        else:
            aux2 = var[i].strip()
            nbr.append(aux2)
    return incognitas, nbr

def ft_get_degree(var):
    max = -1

    for i in range(len(var)):
        for j in range (len(var[i])):
            if (var[i][j] == '^'):
                j += 1
                if max < int(var[i][j]):
                    max = int(var[i][j])
    if max == -1:
        return 1
    return max

def ft_operate_function(expression):
    x = ft_separate_x(expression)
    print("x: ", x)
