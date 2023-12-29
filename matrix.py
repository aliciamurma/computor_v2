
from library import *

def ft_is_matrix(var):
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    if expression.startswith("[[") and expression.endswith("]]"):
        filas = expression[2:-2].split("];[")  # Separate by ;
        el_first_row = filas[0].count(',') + 1
        
        for fila in filas:
            if fila.count(',') + 1 != el_first_row:
                return False
            
        for fila in filas:
            elementos = fila.split(',')
            for elem in elementos:
                try:
                    float(elem.strip())  # Use strip() to remove leading/trailing whitespaces
                except ValueError:
                    return False
        return True
    return False

def ft_print_matrix(var):
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    variable = parts[0].strip()
    expression = parts[1].strip()
    # Dividir cadena en listas de números
    rows = [list(map(int, row.strip('[]').split(','))) for row in expression.split(';')]

    # Imprimir la matriz
    for row in rows:
        print("[", end=" ")
        for num in row:
            print(num, end=" ")
        print("]")


def ft_save_matrix(var):
    print("Save matrix")
    parts = var.split('=')
    if len(parts) != 2:
        raise ValueError("Error in format")
    print("VAR IS: ", parts[0], " ", parts[1])
    name = parts[0].strip()
    value = float(parts[1].strip()) # convierte cadena en objeto
    new_var = MyVar(name, value)
    variables[name] = new_var  # Add the new variable to the 'variables' dictionary
    print("We have saved: ", variables[name])
    ft_find_variable(variables, name)
    # print(ft_find_variable(variables, name))
    print("\n\n")
    ft_print_matrix(var)
