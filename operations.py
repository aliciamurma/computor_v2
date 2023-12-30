from library import *
from aux import *
import re

def ft_operate_numeric(expression):
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

# re.sub busca todas las coincidencias de nombres de variables en la expresión y reemplazarlos con sus respectivos valores
def replace_variables(expression):
    print("INSIDE THE FUNCTION!")
    pattern = r'\b\w+\b'  # Expresión regular para buscar nombres de variables

    def replace(match):
        variable_name = match.group()
        variable_value = ft_find_variable(MyVar, variable_name)
        return str(variable_value) if variable_value is not None else variable_name

    modified_expression = re.sub(pattern, replace, expression)
    return modified_expression

def ft_separate(var):
    # Definir una expresión regular para buscar los símbolos como separadores
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    print("tokens is: ", output_str)
    return output_str

def ft_operate(var):
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    name = parts[0].strip()
    value = parts[1].strip() 
    separated = ft_separate(value)
    replaced = replace_variables(separated)
    print(replaced)