import re
from library import *
from aux import *

def ft_operate_parenthesis(expression):
    print("Operate parenthesis")

def ft_operate(expression):
    operandos = []
    operadores = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit() or (i < len(expression) - 1 and expression[i] == '-' and expression[i + 1].isdigit()):
            # Extraer números (manejar números negativos)
            inicio = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            operandos.append(float(expression[inicio:i]))

        elif expression[i] in "+-*/":
            # Manejar operadores
            while operadores and operadores[-1] in "*/" and (expression[i] in "+-"):
                operador = operadores.pop()
                operando2 = operandos.pop()
                operando1 = operandos.pop()
                if operador == '*':
                    operandos.append(operando1 * operando2)
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
            operadores.pop()  # Sacar el paréntesis izquierdo
            i += 1

        else:
            i += 1

    while operadores:
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

    return operandos[0]


# 1 ()
# 2 ^
# 3 * / %
# 4 + -
def ft_operate_function(expression, variable_value=None):
    expression = re.sub(r'(\d+)([a-zA-Z])', r'\1*\2', expression)  # Agregar "*" entre coeficientes y variables
    expression = re.sub(r'([a-zA-Z])(\d+)', r'\1*\2', expression)  # Agregar "*" entre variables y coeficientes
    expression = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expression)  # Agregar "*" entre variables

    operandos = []
    operadores = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit() or (i < len(expression) - 1 and expression[i] == '-' and expression[i + 1].isdigit()):
            # Extraer números (manejar números negativos)
            inicio = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            operandos.append(float(expression[inicio:i]))

        elif expression[i] in "+-*/":
            # Manejar operadores
            while operadores and operadores[-1] in "*/" and (expression[i] in "+-"):
                operador = operadores.pop()
                operando2 = operandos.pop()
                operando1 = operandos.pop()
                if operador == '*':
                    operandos.append(operando1 * operando2)
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
            operadores.pop()  # Sacar el paréntesis izquierdo
            i += 1

        else:
            i += 1

    while operadores:
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

    if len(operandos) == 1:
        return operandos[0]
    else:
        return "Error: Expresión inválida."



def one_letter(expression):
    letters = filter(str.isalpha, expression.lower())
    n_letters = set(letters)
    return len(n_letters)

def ft_is_function(var):
    print("Inside function")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    if one_letter(expression) != 1:
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
    value = ft_operate_function(value)
    print("VALUE AHORA ES: ", value)
    new_var = MyVar(name, value)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary