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
def ft_expression(var):
    print("VAR IS: ",var)
    spaces = var.split(' ')
    print("THE RESULT IS: ", ft_operate(var))

def ft_save_function(var):
    print("Save function")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    ft_expression(expression)
