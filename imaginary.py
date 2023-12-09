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
    print("INSIDE GET")
    aux = var.split()
    if var[-1] == 'i': # el numero imaginario es el ultimo parametro
        print("var-1 es i ")
        print("aux :-2 es: ", aux[:-1], "imaginary: ", aux[-2:])
        return {"real": aux[:-2], "imaginary": aux[-2:]}
    return {"real": aux[-2:], "imaginary": aux[:-2]}

    '''

    print("MYYY V AR ES: ", var)
    # Patrón de expresión regular para buscar coeficientes imaginarios y reales
    coincidence = re.search(r'\s*([-+]?\s*\d*)\s*i\s*([-+]?\s*\d*)\s*|\s*([-+]?\s*\d+)\s*([-+]?\s*\d*)\s*i\s*', var)
    if coincidence:
        real_part_1, imaginary_part_1, real_part_2, imaginary_part_2 = coincidence.groups()

        # Verificar si el primer grupo tiene la parte imaginaria
        if imaginary_part_1 is not None and imaginary_part_1.strip() != '':
            real_part, imaginary_part = real_part_1.strip(), imaginary_part_1.strip()
        # Verificar si el segundo grupo tiene la parte imaginaria
        elif imaginary_part_2 is not None and imaginary_part_2.strip() != '':
            real_part, imaginary_part = real_part_2.strip(), imaginary_part_2.strip()
        else:
            # No debería llegar aquí si la expresión está bien diseñada
            return {"real": 0, "imaginary": 0}

        # Si la parte imaginaria está vacía, asignarle 0
        imaginary_part = imaginary_part if imaginary_part else '0'

        # Eliminar espacios en blanco y convertir a enteros
        real_part = int(real_part.replace(' ', ''))
        imaginary_part = int(imaginary_part.replace(' ', ''))

        # Ajustar el signo en función del primer carácter
        signo = -1 if var[0] == '-' else 1
        print("Me voy en el primer return")
        # Devolver las partes real e imaginaria
        return {"real": real_part, "imaginary": imaginary_part * signo}

        print("Me voy en el primer return")
        # Devolver las partes real e imaginaria
        return {"real": real_part, "imaginary": imaginary_part * signo}

    print("Me voy en el segundo return")
    # Si no hay coincidencia, devolver ambas partes como 0
    return {"real": 0, "imaginary": 0}
    '''

def ft_print_imaginary(var):
    result = ft_get_imaginary_and_real(var)  
    real_part = "".join(result['real'])
    imaginary_part = "".join(result['imaginary'])

    print(real_part, " ", end="")
    if result['imaginary']:
        first_char_img = result['imaginary'][0]
        if first_char_img != '-':
            print("+", end="")
    print(imaginary_part)


    '''
    print(f"{result['real']}", end=' ')
    if result['imaginary'] < 0:
        print('-', end=' ')
    else:
        print('+', end=' ')
    print(f"{abs(result['imaginary'])}i")
    '''

def ft_save_imaginary(var):
    print("Save imaginary: ", var)
    var2 = var.split('=')
    new_var = MyVar(var2[0], var2[1])
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    ft_print_imaginary(var2[1])

def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    if len(var) != 2:
        return False

    parts = re.split(r'[-+]', var[1])
    
    if var[1][-1] == 'i':
        real = parts[0].strip()
        imaginary = parts[1].strip()
    else:
        real = parts[1].strip()
        imaginary = parts[0].strip()

    try:
        if (real.replace("-", "").replace("+", "").isdigit() and
            (imaginary.replace("-", "").replace("+", "").isdigit() or
            (imaginary[-1] == 'i') and imaginary[:-1].replace("-", "").replace("+", "").isdigit())):
            return True
        else:
            return False
    except ValueError:
        print("except")
        return False
'''
def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    if len(var) != 2:
        return False
    if var[1][-1] == 'i':
        partes = parts = re.split(r'[-+]', var[1])
    else:
        partes = var[1].replace(" ", "").split('i')

    if len(partes) == 2:
        last_pos = 0
        real = partes[0].strip()
        imaginary = partes[1].strip()
        if imaginary[-1] is 'i':
            last_pos = 1
        try:
            if last_pos == 1:
                if (real.replace("-", "").replace("+", "").isdigit() and
                    (imaginary.replace("-", "").replace("+", "").isdigit() or
                    (imaginary[-1] == 'i') and imaginary[:1].replace("-", "").replace("*", "").replace("+", "").isdigit())):
                    return True
            elif (real.replace("-", "").replace("+", "").isdigit() and imaginary.replace("-", "").replace("+", "").replace("*", "").isdigit()):
                return True
            else:
                return False
        except ValueError:
            print("except")
            return False
    return False
'''