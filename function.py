import re
from library import *
from aux import *
from operations import *
from sympy import *

def ft_first_degree(b, c):
    solve = b/c
    return f"Solution: {solve}"

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
    try:
        letters = filter(str.isalpha, expression.lower())
        n_letters = set(letters)
        return len(n_letters)
    except Exception as e:
        print(f"Error evaluating expression {expression}: {e}")
    return False

def ft_get_degree(ecuacion):
    matches = re.findall(r"([-+]?\d*)\s*\*\s*x\^(\d+)", ecuacion) # Utiliza expresiones regulares para encontrar términos con exponentes    
    if not matches:
        return 0 # Si no hay términos con exponentes, el grado es 0

    # Encuentra el exponente máximo
    max_exponente = max(int(match[1]) for match in matches)
    return max_exponente

def ft_print_function(var):
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches) # Construir la cadena de salida uniendo los términos encontrados

    print(output_str)

def ft_is_function(left, right):
    print("Inside is function!")

    if not (len(left) == 7 and left[:3] == "fun" and left[4] == "(" and left[6] == ")" and left[5].isalpha() and left[3].isalpha()):
        return False
    if not ft_one_letter(right):
        print("Error!!")
        return True
    if not ft_is_correct_letter(right, left[5]):
        if "?" in right :
            print("THERE IS AN INTERROGANT!!!")
            return True
      #  print("its not correct letter")
       # return False

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

def ft_pre_solve(var, incognita):
    print("INSIDE PRE SOLVE")
    print("var: ", var)
    print("incognita: ", incognita)
    try:
        var = re.sub(r'\s+', ' ', var)
        var = var.replace(f" * {incognita}", str(incognita))
        var = var.replace(f"* {incognita}", str(incognita))
        var = var.replace(f" *{incognita}", str(incognita))
        var = var.replace(f"*{incognita}", str(incognita))
        var = var.replace(f"{incognita} * ", str(incognita))
        var = var.replace(f"{incognita} *", str(incognita))
        var = var.replace(f"{incognita}* ", str(incognita))
        var = var.replace(f"{incognita}*", str(incognita))
        print("llega?")
        var = var.replace(f"{incognita} ^", f"{incognita}^")
        var = var.replace(f"{incognita}^ ", f"{incognita}^")
        var = var.replace(f" {incognita}", f"{incognita}")
        var = var.replace("+ ", "+")
        var = var.replace("- ", "-")
        var = var.replace("* ", "*")
        var = var.replace("( ", "(")
        var = var.replace(" )", ")")
        print("before first if")
        if var[0].isdigit:
            print("var[0] is: ", var[0])
            if var[0] != '-' and var[0] != '+':
                a = "+"
                var = a + var
        print("var is: ", var)
    except:
        return var
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

    letter = ft_get_incognita_letter(left)
    replaced = ft_pre_solve(real_value.value, letter)
    incog, nbr = ft_separate_x_nbr(replaced, letter)
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
    elif degree == 1:
        solved = ft_first_degree(func_dict.get(1, 0), func_dict.get(0, 0))
        print(solved)

def ft_necessary_operation_incognita(expression, letter):
    try:
        var = expression.split('/')
        part1 = var[0].strip()
        part2 = var[1].strip()
        if letter in part1 and letter in part2:
            return True
    except:
        try:
            var = expression.split('*')
            part1 = var[0].strip()
            part2 = var[1].strip()
            if letter in part1 and letter in part2:
                print("true 2")
                return True
        except:
            #Los parentesis es para preguntar si hay un parentesis (con su correspondiente /)
            #\s* coincide con cero o más caracteres de espacio en blanco
            #(\d+) coincide con 1 o más dígitos (0-9)
            patron = r'\((.*?)\)\s*\^\s*(\d+)'
            coincidences = re.findall(patron, expression)
            print("coincidences: ", coincidences)
            if coincidences:
                for match in coincidences:
                    operacion_elevada = match[0]
                    potencia = int(match[1])
                if letter in operacion_elevada:
                    return True
            return False
    return False

def ft_is_exponential(expression, letter):
    try:
        patron = r'\((.*?)\)\s*\^\s*(\d+)'
        coincidences = re.findall(patron, expression)
        if coincidences:
            for match in coincidences:
                operacion_elevada = match[0]
                potencia = int(match[1])
            if letter in operacion_elevada:
                return True
    except:
        return False

def replace_expr(match):
    return ""

def ft_separate_exponential(input_str, letter):
    input_str = input_str.replace(" ", "") # quitamos espacios

    #pattern = r'\((.*?)\)\^(\d+)'
    pattern = r'([+-]\(.*?\)\^\d+)'
    match = re.search(pattern, input_str)

    if match:
        extracted_expr = match.group(0)
        str_rest = re.sub(pattern, replace_expr, input_str)
        return extracted_expr, str_rest
    return NULL

def ft_get_saver(expression, letter):
    print("inside ft_get_saver")
    incog, nbr = ft_separate_x_nbr(expression, letter)
    #if len(incog) == 0:
    #    print("Error. There is not variables, save it with a rational variable, not a function, stupid.")
    #    return "ERROR"
    if len(nbr) == 0:
        func_dict = ft_get_dictionary(incog, "0", letter)
    else:
        func_dict = ft_get_dictionary(incog, nbr, letter)
    saver = ft_get_expression(func_dict, letter)
    return saver

def ft_save_function(left, right):
    print("save function")
    if "?" in right:
        ft_solve_equation(left, right)
        return 
    letter = ft_get_incognita_letter(left)
    separated = ft_separate(right)
    replaced = ft_replace_variables(separated)
    replaced = ft_pre_solve(replaced, letter)
    print("After pre solve, replaced is:", replaced)
    replaced2 = ft_separate(replaced) #Añadimos aqui un ft_separate para que en ft_necessary_operation_incognita me lo separe bien
    print("After replaced2, which is: ", replaced2)
    if not ft_is_correct_letter(right, left[5]) and "?" not in right:
        print("Error. It is not the correct letter")
        return
    if ft_necessary_operation_incognita(replaced2, letter):
        print("INSIDE ft_necessary_operation_incognita")
        saver = replaced
        if ft_is_exponential(replaced2, letter):
            binomio, expression = ft_separate_exponential(replaced2, letter)
            expression = ft_separate(expression)
            binomio = ft_separate(binomio)
            expression = ft_pre_solve(expression, letter)
            binomio = ft_pre_solve(binomio, letter)
           
            incog, nbr = ft_separate_x_nbr(expression, letter)
            if len(nbr) == 0:
                print("INSIDE NBR IS 0!!!!!, what else?")
                func_dict = ft_get_dictionary(incog, "0", letter)
            else:
                func_dict = ft_get_dictionary(incog, nbr, letter)
            saver = ft_get_expression(func_dict, letter)
            saver_list = saver.split()  # convierte la cadena en una lista de expresiones
            saver_list.append(binomio) # añade el binomio a la lista
            saver = ' '.join(saver_list) # volver a unir la listaçen una cadena
    else:
        print("INSIDE ELSE")
        print("Vamos a expandir: ", replaced)
        # OJOOO, saver es un sympy.Expr, no una cadena!!!!
        # Podemos utilizar subs en vez de replace
        # Como despues tenemos que guardarlo, mejor lo convertimos rimero en cadena
        saver1 = expand(replaced)
        print("saver: ", saver1)
        print("letter: ", letter)
        saver = str(saver1)
        saver = saver.replace(f" * {letter}", str(letter))
        print("NI AL PRIMER REPLACE")
        saver = saver.replace(f"* {letter}", str(letter))
        saver = saver.replace(f" *{letter}", str(letter))
        saver = saver.replace(f"*{letter}", str(letter))
        saver = saver.replace(f"{letter} * ", str(letter))
        saver = saver.replace(f"{letter} *", str(letter))
        saver = saver.replace(f"{letter}* ", str(letter))
        saver = saver.replace(f"{letter}*", str(letter))
        print("result: ", saver)
        #saver = ft_get_saver(result, letter)
        #if saver == "ERROR":
        #    return
    name = left[:4] if len(left) >= 4 else left
    new_var = MyVar(name, saver)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary
    real_value = ft_find_variable(variables, name)
    if real_value:
        print(real_value.value)

def ft_get_expression(incog, letter):
    result = []  # Inicializa como lista vacía
    for key, value in incog.items():
        sign = '+' if value >= 0 else ''  # Determina el signo del valor
        if key != 0:
            aux = f"{value}" + letter + f"^{key}"  # f-strings para formatear la expresión
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
    var2_value = eval(num_str)
    if var2_value != 0:  # NO incluir var2 si es igual a 0
        incog[0] = var2_value

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

def ft_separate_x_nbr(var, letter):
    incognitas = []
    nbr = []
    print("var FIRST is: ", var)
    var = var.split(' ')

    # Definir una expresión regular para buscar los símbolos como separadores
    try:
        for i in range(len(var)):
            if letter in var[i]:
                aux1 = var[i].strip()
                incognitas.append(aux1)
            else:
                aux2 = var[i].strip()
                print("aux2 is: ", aux2)
                nbr.append(aux2)
                print("nbr is: ", nbr)
    except:
        return var
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
