from library import *
from aux import *
from function import *
import re

def ft_operate_numeric2(expression):
    operandos = []
    operadores = []
    i = 0
    negative = 0
    nbr_neg = 0

    while i < len(expression):
        if i == 0 and expression[0] == '+':
            i += 1
        if i == 0 and expression[0] == '-':
            negative = 1
            nbr_neg = expression[2]
            i += 1
        if expression[i].isdigit() or (i < len(expression) - 1 and expression[i] == '-' and expression[i + 1].isdigit()):
            # Extraer números (manejar números negativos)
            inicio = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            operandos.append(float(expression[inicio:i]))

        elif expression[i] in "+-*/%":
            # Manejar operadores
            while operadores and operadores[-1] in "*/%" and (expression[i] in "+-"):
                operador = operadores.pop()
                operando2 = operandos.pop()
                operando1 = operandos.pop()
                if operador == '*':
                    operandos.append(operando1 * operando2)
                if operador == '%':
                    operandos.append(operando1 % operando2)
                elif operador == '/':
                    if operando2 != 0:
                        operandos.append(operando1 / operando2)
                    else:
                        return "Error: No se puede dividir por cero."

            operadores.append(expression[i])
            i += 1

        elif expression[i] == '(':
            operadores.append(expression[i])
            i += 1

        elif expression[i] == ')':
            while operadores and operadores[-1] != '(':
                operador = operadores.pop()
                operando2 = operandos.pop()
                operando1 = operandos.pop()
                if operador == '+':
                    operandos.append(operando1 + operando2)
                elif operador == '-':
                    operandos.append(operando1 - operando2)
                elif operador == '*':
                    operandos.append(operando1 * operando2)
                elif operador == '/':
                    if operando2 != 0:
                        operandos.append(operando1 / operando2)
                    else:
                        return "Error: No se puede dividir por cero."
                elif operador == '%':
                    operandos.append(operando1 % operando2)
            operadores.pop()  # Sacar el paréntesis izquierdo
            i += 1

        else:
            i += 1

    while operadores:
        operando2 = operandos.pop()
        operando1 = operandos.pop()
        operador = operadores.pop()
        if operador == '+':
            if negative == 1 and nbr_neg.strip() and operando1 == float(nbr_neg.strip()):
                negative = 0
                print("-", operando1, "+", operando2)
                operandos.append(- operando1 + operando2)
            else:
                operandos.append(operando1 + operando2)
                print(operando1, "+", operando2)
        elif operador == '-':
            if negative == 1 and nbr_neg.strip() and operando1 == float(nbr_neg.strip()):
                negative = 0
                operandos.append(- operando1 - operando2)
                print("-", operando1, "-", operando2)
            else:
                operandos.append(operando1 - operando2)
                print(operando1, "-", operando2)
        elif operador == '*':
            operandos.append(operando1 * operando2)
            print(operando1, "*", operando2)
        elif operador == '/':
            if operando2 != 0:
                operandos.append(operando1 / operando2)
                print(operando1, "/", operando2)
            else:
                return "Error: No se puede dividir por cero."
    return operandos[0]

def ft_isletter(var):
    return any(caracter.isalpha() for caracter in var)

def ft_separate(var):
    pattern = r'\b(?:\d+\.\d+|\w+)\b|[()+\-^*/%]' # \d+\.\d+ coincide con números decimales
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)

    # Encuentra y separa los términos elevados a un exponente
    matches_with_exponents = re.findall(r'\w+\s*\^\s*\d+', output_str)
    for match in matches_with_exponents:
        output_str = output_str.replace(match, ' ' + match + ' ')

    return output_str

'''
def ft_separate(var):
    # Definir una expresión regular para buscar los símbolos como separadores
    pattern = r'\b(?:\d+\.\d+|\w+)\b|[()+\-^*/%]' # \d+\.\d+ coincide con números decimales
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str
'''
def ft_get_nbr(var):
    var = var.split(' ')
    for i in range(len(var)):
        if var[i] == '(':
            i += 1
            return var[i]
    return 0

def ft_find_letter_function(var):
    for i in range(len(var)):
        if var[i].isalpha():
            return var[i]

def ft_replace_letter(var):
    i = 0
    replaced = []
    updated_var = ""
    
    nbr = ft_get_nbr(var)
    letter = ft_find_letter_function(var)
    print("nbr is: ", nbr)
    print("The letter is: |", letter)
    while i < len(var) - 5:
        print("var i: ", var[i])
        if (var[i] == '(' and i + 1 < len(var) and var[i + 1] == letter):
            replaced.append(var[i])
            replaced.append(letter)
            i += 2
        elif (var[i] == letter):
            print("INSIDEEE")
            replaced.append(" ")
            replaced.append("*")
            replaced.append(" ")
            replaced.append(letter)
            i += 1
        else:
            replaced.append(var[i])
            i += 1
    #updated_var = var.replace(letter, " * " + str(nbr))
    #updated_var = re.sub(r'\([^)]*\)', '', updated_var)
    replaced_str = ''.join(replaced)
    replaced_str = replaced_str.replace("^", " ** ")
    print("UPDATED VAR IS: ", replaced_str)
    #replaced = replaced.replace("^", " ** ")
    return replaced_str

def calculate_sum(functions, values):
    total = 0
    for i, fun in enumerate(functions):
        total += fun(values[i])
    return total

def ft_replaced_incognitas(var):
    parts = var.split(' ')
    if len(parts) == 0:
        print("WTF?????")
        return
    for part in parts:
        part = part.strip()
        if part in variables:
            return str(variables[part].value)

def ft_get_number_functions(var):
    i = 0
    count = 0

    while i < len(var) - 3:  # Se resta 3 para evitar índices fuera de rango
        if var[i:i+3] == "fun" and var[i+3].isalpha():
            i = i + 3
            count += 1
        i += 1
    print("umerp de veces encon trado: ", count)
    return count

def ft_chopping_functions(var):
    print("entro en ft_chopping_functions")
    # búsqueda: 'fun' + letra + '(' + dígito + ')'
    #patron = r'fun\w\(\s*\d+\s*\)'
    patron = r'fun\w\s*\(\s*\d+\s*\)'
    partes = re.findall(patron, var) # finds *all* the matches and returns them as a list of strings
    return partes

def ft_replaced_function(var, letra):
    patron = r'\(\s(\d+)\s\)'
    # Utilizamos re.sub() para reemplazar 
    new_replaced = re.sub(patron, f'({nuevo_numero})', var)
    match = re.search(patron, var)
    if match:
        numero = match.group(1)  # Obtenemos el número capturado por la expresión regular
        new_replaced = var.replace(letra, numero)
        return new_replaced

def ft_operate(left, right):
    print("Inside operate :D")
    separated = ft_separate(right)
    replaced = ft_replace_variables(separated)
    
    if ft_have_function(separated) is True:
        nbr_funct = ft_get_number_functions(separated)
        
        i = 0
        result = []
        chopped = [None] * nbr_funct
        chopped = ft_chopping_functions(separated)
        print("chopped: ", chopped)
        while i < nbr_funct:
            print("chopped[i]: ", chopped[i])
            replaced_function = ft_replace_letter(ft_replace_variables(chopped[i]))
            print("ttthere the replaced is: ", replaced_function)
            final_result = eval(replaced_function)
            print("final result is: ", final_result)
            result.append(final_result)
            print("result: ", result)
            i += 1
        print("OUT OF WHILE, BYE BYE")
        return

    if ft_isletter(replaced) is False:
        replaced = replaced.replace("^", "**")
        operated = eval(replaced)
        print("the  operate: ", operated)
        new_var = MyVar(left, operated)
        variables[left] = new_var
        value = ft_find_variable(variables, left)
        print(value.value)
    elif ft_one_letter(replace) is True:
        print("No please, no.")
    else:
        print("I cannot do that operation")
