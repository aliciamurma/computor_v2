from library import *
import re


def ft_get_imaginary(var):
    # Patrón de expresión regular para buscar coeficientes imaginarios
    coincidence = re.search(r'([-+]?\s*\d*)i', var)
    if coincidence:
        # Obtener el coeficiente imaginario
        nbr_i = coincidence.group(1)
        # Si el coeficiente es vacío o solo tiene un signo, asignarle 1
        if not nbr_i or nbr_i == '+' or nbr_i == '-':
            nbr_i = '1'
        # Si el coeficiente es '-' sin dígito, asignarle -1
        elif nbr_i == '-':
            nbr_i = '-1'
        # Eliminar espacios en blanco y convertir el coeficiente a un número
        nbr_i = int(nbr_i.replace(' ', ''))
        # Verificar el signo
        signo = -1 if var[0] == '-' else 1
        return nbr_i * signo
    return 0

def ft_get_imaginary_and_real(var):
    # Patrón de expresión regular para buscar coeficientes imaginarios y reales
    coincidence = re.search(r'([-+]?\s*\d*)i\s*([-+]?\s*\d*)', var)
    if coincidence:
        nbr_i = coincidence.group(1) # Obtener el coeficiente imaginario
        # Si no hay o solo tiene un signo, asignarle 1
        if not nbr_i or nbr_i == '+' or nbr_i == '-':
            nbr_i = '1'
        # Si el coeficiente es '-' sin dígito, asignarle -1
        elif nbr_i == '-':
            nbr_i = '-1'
        # Eliminar espacios en blanco y convertir el coeficiente a un número
        nbr_i = int(nbr_i.replace(' ', ''))
        real_part = coincidence.group(2)

        # Si el componente real es vacío o solo tiene un signo, asignarle 0
        if not real_part or real_part == '+' or real_part == '-':
            real_part = '0'      
        # Eliminar espacios en blanco y convertir el componente real a un número
        real_part = int(real_part.replace(' ', ''))
        signo = -1 if var[0] == '-' else 1
        return {"real": real_part, "imaginary": nbr_i * signo}
    # Si no se encuentra ninguna coincidencia, el componente real e imaginario son ambos 0
    return {"real": 0, "imaginary": 0}

def ft_print_imaginary(var):
    result = ft_get_imaginary_and_real(var)
    print(f"{result['real']}", end=' ')
    if result['imaginary'] < 0:
        print('-', end=' ')
    else:
        print('+', end=' ')
    print(f"{abs(result['imaginary'])}i")

def ft_save_imaginary(var):
    print("Save imaginary")
    var2 = var.split('=')
    new_var = MyVar(var2[0], var2[1])
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    ft_print_imaginary(var2[1])

def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    if len(var) != 2:
        return False
    x = var[1].find("i")
    print("X ES: ", x, "LA ULT POS ES: ", len(var[1]))
    if (x != len(var[1]) -1):
        partes = var[1].replace(" ", "").split('i')
    if (x == len(var[1]) -1 and var[x -2] == '*'):
        partes = var[1].replace(" ", "").split('i')
    else:
        print("ESTOY EN ULTIMA PSOICION!")
    print("PARTES IS: ",  x)

    if len(partes) == 2:
        real = partes[0].strip()
        imaginary = partes[1].strip()
        print("The real len is: ", len(real))
        #  and real[len(real)] == '*') or (real[0] == '-' and real[1:len(real)-1].isdigit() and real[len(real)] == '*')
        try:
            if (real.isdigit() or (real[:1].isdigit())
                    (real[0] == '-' and real[1:].isdigit())) and (imaginary.isdigit() or
                                                                 (imaginary[0] == '-' and imaginary[1:].isdigit())):
                print("INSIDE")
                return True
            else:
                return False
        except ValueError:
            print("except")
            return False
    return False
