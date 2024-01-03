from library import *
from aux import *
from function import *
import re

def ft_operate_numeric(expression):
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
        operando2 = operandos.pop()
        operando1 = operandos.pop()
        operador = operadores.pop()
        if operador == '+':
            if negative == 1 and nbr_neg.strip() and operando1 == float(nbr_neg.strip()):
                negative = 0
                operandos.append(- operando1 + operando2)
            else:
                operandos.append(operando1 + operando2)
        elif operador == '-':
            if negative == 1 and nbr_neg.strip() and operando1 == float(nbr_neg.strip()):
                negative = 0
                operandos.append(- operando1 - operando2)
            else:
                operandos.append(operando1 - operando2)
        elif operador == '*':
            operandos.append(operando1 * operando2)
        elif operador == '/':
            if operando2 != 0:
                operandos.append(operando1 / operando2)
            else:
                return "Error: No se puede dividir por cero."
    return operandos[0]

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
        print(ft_operate_numeric(replaced))
    elif ft_one_letter(replace) is True:
        print("No please, no.")
    else:
        print("I cannot do that operation")
