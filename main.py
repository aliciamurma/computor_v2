import sys
import re

variables = {}

def ft_check_statement(statement):
    var2 = statement.split('=')
    if len(var2) != 2:
        print("Error in syntax")
        sys.exit(-1)

def ft_is_variable(var):
    var2 = var.split('=')
    if len(var2) == 2:
        return (True)
    return (False)

def ft_is_rational_numer(var):
    print("Inside is rational")
    var2 = var.split('=')
    if len(var2) != 2:
        return (False)
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    if right_side.isdigit():
        return (True)
    return (False)

def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    if len(var) != 2:
        return (False)
    partes = var[1].replace(" ", "").split('i')

    print("partes is: ", len(partes))
    if len(partes) == 2:
        real = partes[0].strip()
        imaginary = partes[1].strip()
        try:
            if real.isdigit() or (real[0] == '-' and real[1:].isdigit()):
                float(imaginary)
                return (True)
            else:
                float(real)
                float(imaginary)
            return True
        except ValueError:
            return False
    return False

def ft_is_matrix(var):
    print("Inside is matrix")
    if var.startswith("[[") and var.endswith("]]"):
        filas = var[2:-2].split("];[") #Separate by ;
        el_first_row = filas[0].count(',') + 1
        for fila in filas:
            if fila.count(',') + 1 != el_first_row:
                return False
        for fila in filas:
                elementos = fila.split(',')
        for elem in elementos:
            try:
                float(elem)
            except ValueError:
                return False
        return True
    return False

def evaluate_expression(expression):
    global variables
    # Replace variable names with their values
    for var in variables:
        expression = re.sub(r'\b' + var + r'\b', str(variables[var]), expression)
    # Evaluate the expression
    result = eval(expression)
    return result

def ft_is_function(var):
    print("Inside is function")
    global variables

    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")

    variable = parts[0].strip()
    expression = parts[1].strip()
    # Check if it's a function definition
    if '(' in variable and ')' in variable:
        function, parameters = variable.split('(')
        parameters = parameters.replace(')', '').strip()
        variables[function.strip()] = lambda *args: evaluate_expression(expression.format(*args))
    else:
        variables[variable] = evaluate_expression(expression)


def ft_save_imaginary(var):
    print("Save imaginary")

def ft_save_rational(var):
    print("Save rational")

def ft_save_matrix(var):
    print("Save matrix")

def ft_save_function(var):
    print("Save function")

def ft_save_variable(var):
    if ft_is_rational_numer(var):
        ft_save_rational(var)
    elif ft_is_imaginary(var):
        ft_save_imaginary(var)
    elif ft_is_matrix(var):
        ft_save_matrix(var)
    elif ft_is_function(var):
        ft_save_function(var)

def ft_process_statement(statement):
    print("Before check")
    ft_check_statement(statement)
    if (ft_is_variable(statement)):
        ft_save_variable(statement)

def ft_start():
    while True:
        prompt = input("Enter a statement: ")
        while not prompt:
            prompt = input("Enter a statement: ")
        ft_process_statement(prompt)

def main(argv):
    try:
        if len(argv) == 1:
            ft_start()
    except error as e:
        print("Error\n", e);

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
