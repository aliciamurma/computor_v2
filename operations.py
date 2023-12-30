from library import *
from aux import *
from function import *
import re

def ft_operate_numeric(expression):
    operandos = []
    operadores = []
    i = 0

    while i < len(expression):
        if expression[i].isdigit() or (i < len(expression) - 1 and expression[i] == '-' and expression[i + 1].isdigit()):
            # Extraer números (manejar números negativos)
            print("INSIDE FIRST IF")
            inicio = i
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            operandos.append(float(expression[inicio:i]))

        elif expression[i] in "+-*/":
            print("INSIDE SECOND IF")
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

def ft_replace_variables(var):
    parts = var.split(' ')
    if len(parts) == 0:
        print("?????")
        return

    new = []
    for part in parts:
        if part in variables:
            new.append(variables[part].value)
        else:
            new.append(part)
    result = ' '.join(new)
    return result

def ft_isletter(var):
    return any(caracter.isalpha() for caracter in var)

def ft_separate(var):
    # Definir una expresión regular para buscar los símbolos como separadores
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str

def ft_operate(var):
    print("Inside operate :D")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    name = parts[0].strip()
    value = parts[1].strip()

    separated = ft_separate(value)
    replaced = ft_replace_variables(separated)
    if ft_isletter(replaced) is False:
        print("Inside one letter")
        print("result: ", ft_operate_numeric(replaced))
'''
    else:
        print("I cannot do that operation")
'''