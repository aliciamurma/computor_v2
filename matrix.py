
from library import *
from aux import ft_find_variable

def ft_is_matrix(left, right):
    print("Inside is matrix")
    if right.startswith("[[") and right.endswith("]]"):
        return True
    return False

def ft_correct_rows(matrix):
    print("inside ft_is_correct_rows")
    if matrix.startswith("[[") and matrix.endswith("]]"):
        filas = matrix[2:-2].split("];[")  # Separate by ;
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

def ft_square_matrix(matrix_raw):
    print("inside ft_square_matrix")
    matrix = matrix_raw.replace("[", "")
    matrix = matrix.replace("]", "")
    print("MATRIX IS:", matrix)
    if ';' in matrix:
        filas = matrix.split(';')
        columns = len(filas[0].split(','))
        for fila in filas:
            elementos = fila.split(',') #miramos que tengan comas
        if len(elementos) != columns:
            return False
        for elemento in elementos: #checkea que sean numeros convirtiendo esa parte del string en un numero
            print("en el for ese chungo: ", elemento)
            try:
                float(elemento)
            except ValueError:
                return False
    return True

def ft_is_correct_matrix(left, right):
    print("inside ft_is_correct_matrix")
    if ft_correct_rows(right) is False:
        print("Thats not a correct matrix bcof the rows")
        return False

    if ft_square_matrix(right) is False:
        print("Thats not a correct matrix bc its not square")
        return False
    print("LETS GOOOO TO SAVE IT")
    return True

'''
    if ft_is_correct_comas(right) is False:
        print("Thats not a correct matrix bcof the comas")
        return False'''

def ft_print_matrix(var):
    rows = [list(map(int, row.strip('[]').split(','))) for row in var.split(';')]

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
    # value = ft_find_variable(variables, left)
    ft_print_matrix(right)

def ft_mutiplicatible_matrix(var):
    return True