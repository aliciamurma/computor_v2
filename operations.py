from library import *
from aux import *
from function import *
from matrix import *
from imaginary import *
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

def ft_separate1(var):
    pattern = r'\[\[|\]\]|\b(?:\d+\.\d+|\w+)\b|[()+\-^*/%]|[\[\]]'
#    pattern = r'\b(?:\d+\.\d+|\w+)\b|[()+\-^*/%]|[\[\]]' # \d+\.\d+ coincide con números decimales
    #OJO que si hacemos re.findall me elimina los corchetes, y tendremos problemas con las matrices
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)

    # Encuentra y separa los términos elevados a un exponente
    matches_with_exponents = re.findall(r'\w+\s*\^\s*\d+', output_str)
    for match in matches_with_exponents:
        output_str = output_str.replace(match, ' ' + match + ' ')

    return output_str

def ft_separate(var):
    pattern = r'\[\[.*?\]\]|\b(?:\d+\.\d+|\w+)\b|[()+\-^*/%]|,|[\[\]]'
    #pattern = r'\[\[.*?\]\]|\b(?:\d+\.\d+|\w+)\b|[+\-^*/%]|,|[\[\]]'

    #pattern = r'\b(?:\d+\.\d+|\d+|\w+)\b|[()+\-^*/%,]|[\[\]]' # \d+\.\d+ coincide con números decimales
    #OJO que si hacemos re.findall me elimina los corchetes, y tendremos problemas con las matrices
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches) 

    # Encuentra y separa los términos elevados a un exponente
    matches_with_exponents = re.findall(r'\w+\s*\^\s*\d+', output_str)
    for match in matches_with_exponents:
        output_str = output_str.replace(match, ' ' + match + ' ')

    # Limpia espacios extra entre operadores y números
    output_str = re.sub(r'\s+', ' ', output_str).strip()

    return output_str

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
    while i < len(var) - 5:
        if (var[i] == '(' and i + 1 < len(var) and var[i + 1] == letter):
            replaced.append(var[i])
            replaced.append(nbr)
            i += 1
        elif (var[i] == letter):
            replaced.append(" ")
            replaced.append("*")
            replaced.append(" ")
            replaced.append(nbr)
        else:
            replaced.append(var[i])
        i += 1
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

# cuando tenemos entre parentesis un digito, queremos trocear cada incognita con su sustituto
def ft_chopping_functions(var):
    print("entro en ft_chopping_functions con: ", var)
    patron = r'\(\s*\d+\s*\)'
    partes = re.split(f'({patron})', var)
    resultado = []
    acumulador = ""

    for parte in partes:
        if re.search(patron, parte):
            acumulador += parte.strip()  # Agregar la parte con el patrón
            resultado.append([acumulador])  # Agregar al resultado
            acumulador = ""  # Resetear el acumulador
        else:
            acumulador += parte  # Acumular partes sin el patrón

    # Si queda algo sin agregar (por si no termina en un número entre paréntesis)
    if acumulador:
        resultado.append([acumulador.strip()])
    return resultado
'''
    for parte in partes:
        acumulador += parte
        if re.search(patron, parte):
            resultado.append([acumulador.strip()])  # Cada sublista contiene una porción completa
            acumulador = ""

    # Si queda algo sin agregar (por si no termina en un número entre paréntesis)
    if acumulador:
        resultado.append([acumulador.strip()])
    print("EL RESULTADO DENTRO DE CHOPPING ES: ", resultado)
    r '''

def ft_replaced_function(var, letra):
    patron = r'\(\s(\d+)\s\)'
    # Utilizamos re.sub() para reemplazar 
    new_replaced = re.sub(patron, f'({nuevo_numero})', var)
    match = re.search(patron, var)
    if match:
        numero = match.group(1)  # Obtenemos el número capturado por la expresión regular
        new_replaced = var.replace(letra, numero)
        return new_replaced

def ft_classify_operations(var):
    result = matrices[0]
    for i, operacion in enumerate(operations):
        if i == '+':
            ft_suma_matrix(result, matrices[i + 1])
        if i == '-':
            ft_suma_matrix(result, matrices[i + 1])
        if i == '*':
            ft_multiplication_matrix(result, matrices[i + 1])

# map(str, fila): Convierte cada elemento de la fila en una cadena.
def ft_from_matrix_to_str(matrix):
    filas_como_cadenas = ['[' + ','.join(map(str, fila)) + ']' for fila in matrix]
    matrix_formato = '[' + ';'.join(filas_como_cadenas) + ']'
    return matrix_formato

def ft_operate_matrix_multip(raw):
    retorno = ''
    idx = 0
    nbr = 0
    raw = raw.replace('* *', '**')
    print("RAW NOW IS: ", raw)
    var = raw.split(' ')

    # for idx, element in enumerate(var)
    # nbr 0 for normal numbers --> EVAL
    # nbr 1 for first matrix and then number 
    # nbr 2 for first number and then matrix
    # nbr 3 for both matrix 
    try:
        while idx < len(var):
            print("while..")
            element = var[idx]
            if idx > 0 and var[idx] == '**':
                if ft_is_matrix("fun", var[idx - 1]) is True and ft_is_matrix("fun", var[idx + 1]) is True:
                    print("YES, IT IS A MATRIX MULTIPLICATION")
                    print("var[idx - 1]", var[idx - 1])
                    print("var[idx + 1]", var[idx + 1])
                    matrix_str = var[idx - 1].replace(";", ',')
                    matrix1 = np.array(eval(matrix_str))
                    matrix_str = var[idx + 1].replace(";", ',')
                    matrix2 = np.array(eval(matrix_str))
                    print("before the np.dot")
                    result = np.dot(matrix1, matrix2)
                    retorno += ft_from_matrix_to_str(result)
                    idx += 1
                print("hemos podido hacer la multiplicacion")
            elif idx > 0 and var[idx] == '*':
                print("vamos a hacer una multiplicacion")
                if ft_is_matrix("fun", var[idx - 1]) is True:
                    print("inside ft_is_matrix -1", var[idx - 1])
                    matrix_str = var[idx - 1].replace(";", ',')
                    matrix1 = np.array(eval(matrix_str))
                    nbr = 1
                if ft_is_matrix("fun", var[idx + 1]) is True:
                    matrix_str = var[idx + 1].replace(";", ',')
                    matrix2 = np.array(eval(matrix_str))
                    if nbr == 1:
                        nbr = 3
                    else:
                        nbr = 2
                if nbr == 3:
                    result = np.dot(matrix1, matrix2)
                elif nbr == 1:
                    result = matrix1 * float(var[idx + 1])
                elif nbr == 2:
                    result = matrix2 * float(var[idx - 1])
                else:
                    retorno += element  # Concatenamos el elemento si no es matriz
                # Convertimos el resultado de nuevo a la cadena
                retorno += ft_from_matrix_to_str(result)
                idx += 1

            elif var[idx + 1] != '*' and var[idx + 1] != '**':
                retorno += element  # Concatenamos el elemento si no es matriz
            idx += 1
            print("IDX: ", idx)
    except:
        print("We cannot operate this matrix")
        return "NP"
    return retorno

# 1o las multiplicaciones de matrices
# 2o los exponentes de matrices
def ft_operate_matrix(var):
    result = ft_operate_matrix_multip(var)
    if result == "NP":
        return var
    print("RESULT: ", result)
    return result

def ft_have_matrix(var):
    print("var is: ", var)
    for i in range(len(var) - 2):
        if var[i] == '[' and var[i + 1] == '[':
            return True
    return False

def ft_have_i(raw):
    for i in range(len(raw)):
        print("var[i]: ", raw[i])
        if raw[i] == 'i':
            return True
    return False

def ft_operate_i(raw):
    print("raw is: ", raw)
    raw = raw.replace("*j", "j")
    raw = raw.replace(" * i", "j")
    raw = raw.replace("* i", "j")
    raw = raw.replace("i", "j")
    raw = raw.replace("^", "**")
    try:
        #operar
        result = eval(raw)
        print("result is: ", result)
        return result
    except Exception as e:
        return f"Error en la operación: {e}"

def ft_operate(left, right, flag):
    print("Inside operate :D: ", right)
    separated = ft_separate(right)
    replaced = ft_replace_variables(separated)
    print("SEPARATED: ", separated)
    print("REPLACED: ", replaced)

    if ft_have_function(separated) == True:
        nbr_funct = ft_get_number_functions(separated)        
        i = 0
        result = []
        operators = []
        chopped = ft_chopping_functions(replaced)
        # Recorremos cada sublista en chopped
        for sublist in chopped:
            for element in sublist:
                print("elemento: ", element)
                # aqui el problema, no replace letter
                replaced_function = ft_replace_letter(element)
                #replaced_function = ft_replace_letter(ft_replace_variables(element))
                print("replaced_function: ", replaced_function)
                # miramos el signo que tiene, porque replaced_function[0] no tiene por que coger un negativo, 
                # forma parte de la cadena, pero no del chopped
                if replaced_function and i != 0:
                    operators.append(replaced_function[0])

                if len(replaced_function) != 0:
                    result.append(replaced_function)
                else:

                    result.append(element)
                i += 1
        #juntar todo en una sola string para poder hacer eval
        #NO juntar con "join", porque es una lista, no una cadena de texto
        final_result = ' '.join(map(str, result))
        operation = eval(final_result)            
        print("RESULT IS: ", operation)
        return operation

    elif ft_have_matrix(replaced) is True:
        result = ft_operate_matrix(replaced)
        if flag is True:
            ft_save_operation(left, result)

    elif ft_have_i(replaced) is True:
        result = ft_operate_i(replaced)
        if flag is True:
            ft_save_operation(left, result)

    elif ft_isletter(replaced) == False:
        replaced = replaced.replace("^", "**")
        operated = eval(replaced)
        ft_save_operation(left, operated)
    else:
        print("I cannot do that operation")
    '''
    if ft_one_letter(replaced) == True:
        print("Nope.")
    '''

def ft_save_operation(left, right):
    print("Save operation")
    new_var = MyVar(left, right)
    variables[left] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, left)
    print(value.value)
