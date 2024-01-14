
from library import *
from aux import ft_find_variable

def ft_is_matrix(left, right):
    print("Inside is matrix")
    if right.startswith("[[") and right.endswith("]]"):
        filas = right[2:-2].split("];[")  # Separate by ;
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

def ft_save_matrix(left, right):
    print("Save matrix")
    new_var = MyVar(left, right)
    variables[left] = new_var  # Add the new variable to the 'variables' dictionary
    value = ft_find_variable(variables, left)
    print(value.value)
    # ft_print_matrix(var)
