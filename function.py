import re
from library import *
from aux import *
from operations import *

def ft_second_degree(a, b, c):
    discriminating = b**2 - 4*a*c

    if discriminating > 0:
        x1 = (-b + math.sqrt(discriminating)) / (2*a)
        x2 = (-b - math.sqrt(discriminating)) / (2*a)
        return f"Two solutions: {x1} , {x2}"
    elif discriminating == 0:
        x = -b / (2*a)
        return f"One solution: {x}"
    else:
        real = -b / (2*a)
        imaginary = math.sqrt(abs(discriminating)) / (2*a)
        solucion1 = f"{real} + {imaginary}i"
        solucion2 = f"{real} - {imaginary}i"
        return f"Complex solutions: {solucion1}, {solucion2}"

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

def ft_is_function(left, right):
    print("Inside is function!")

    if not (len(left) == 7 and left[:3] == "fun" and left[4] == "(" and left[6] == ")" and left[5].isalpha() and left[3].isalpha()):
        return False
    if not ft_one_letter(right):
        error = 1
        return False
    if not ft_is_correct_letter(right, left[5]):
        if "?" in right :
            print("THERE IS AN INTERROGANT!!!")
            return True
        print("its not correct letter")
        error = 1
        return False

    # Find the variable dynamically
    variables = [c for c in right if c.isalpha()]
    if not variables:
        return False
    
    variable = variables[0]  # Take the first letter found as the variable
    parameters = right.split(variable)[1].split(":")[0]
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

def ft_solve_equation(left, right):
    separated = ft_separate(right)
    if len(right) > 3:
        print("No. Just no.")
        return
    replaced_r = ft_replace_variables(separated[0])
    real_value = ft_find_variable(variables, left[:4])
    if real_value:
        print(real_value.value)

    replaced = ft_pre_solve(real_value.value)
    incog, nbr = ft_separate_x_nbr(replaced)
    degree = ft_get_degree(incog)
    if degree > 2:
        print("I dont have to solve it, sorrrry")
        return
    equation = replaced + " = " + replaced_r
    print(left[5])
    func_dict = ft_get_dictionary(incog, nbr, left[5])
    if degree == 2:
        solved = ft_second_degree(func_dict.get(2, 0), func_dict.get(1, 0), func_dict.get(0, 0))
        print(solved)

def ft_save_function(left, right):
    print("save function")
    if "?" in right:
        ft_solve_equation(left, right)
        return 
    letter = ft_get_incognita_letter(left)
    separated = ft_separate(right)
    replaced = ft_replace_variables(separated)
    replaced = ft_pre_solve(replaced)
    incog, nbr = ft_separate_x_nbr(replaced)
    degree = ft_get_degree(incog)
    func_dict = ft_get_dictionary(incog, nbr, letter)
    saver = ft_get_expression(func_dict)
    name = left[:4] if len(left) >= 4 else left
    new_var = MyVar(name, saver)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary
    print("check in the dictionary")
    real_value = ft_find_variable(variables, name)
    if real_value:
        print(real_value.value)

def ft_get_expression(incog):
    result = []  # Inicializa como lista vacía
    for key, value in incog.items():
        sign = '+' if value >= 0 else ''  # Determina el signo del valor
        if key != 0:
            aux = f"{value}x^{key}"  # f-strings para formatear la expresión
        else:
            aux = f"{value}"
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

    for i in range(len(var1)):
        aux = var1[i].split(letter)
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
