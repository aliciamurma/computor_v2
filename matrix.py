
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

def ft_save_matrix(var):
    print("Save matrix")