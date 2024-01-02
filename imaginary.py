from library import *
from aux import *
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
        return {"real": aux[:-2], "imaginary": aux[-2:]}
    return {"real": aux[-2:], "imaginary": aux[:-2]}

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

def ft_save_imaginary(var):
    print("Save imaginary: ", var)
    var2 = var.split('=')
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    right_side = ft_separate_i(right_side)
    replaced = ft_replace_variables(right_side)
    new_var = MyVar(var2[0], replaced)
    variables[var2[0]] = new_var  # Add the new variable to the 'variables' dictionary
    ft_print_imaginary(replaced)

def agrupar_terminos(cadena):
    # Utilizamos expresiones regulares para separar los términos
    terminos = re.findall(r'(-?\d*\.?\d*)?[ij]|\d+|-?\d*\.?\d*', cadena)
    
    # Inicializamos las partes real e imaginaria
    parte_real = 0
    parte_imaginaria = 0

    # Iteramos sobre los términos y sumamos las partes real e imaginaria
    for termino in terminos:
        if 'i' in termino:
            # Si el término contiene 'i', es parte imaginaria
            parte_imaginaria += complex(0, float(termino.replace('i', '')))
        else:
            # Si no contiene 'i', es parte real
            parte_real += float(termino)

    # Formateamos el resultado
    resultado = f"{parte_real} {'+' if parte_imaginaria.imag >= 0 else '-'} {abs(parte_imaginaria.imag)}i"

    return resultado

def ft_separate_i(var):
    # Definir una expresión regular para buscar los símbolos como separadores
    pattern = r'\b\w+\b|[()+\-^*/%]|i'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str

def ft_is_imaginary(var):
    print("Inside is imaginary")
    var = var.split('=')
    if len(var) != 2:
        return False
    right_side = var[1].strip()  # Elimina espacios en blanco alrededor
    right_side = ft_separate_i(right_side)
    replaced = ft_replace_variables(right_side)
    if replaced.find("i") == -1:
        return False
    parts = re.split(r'[-+]', replaced)
    if len(parts) != 2:
        return False
    if replaced[-1] == 'i':
        real = parts[0].strip()
        imaginary = parts[1].strip()
    else:
        real = parts[1].strip()
        imaginary = parts[0].strip()

    try:
        if (real.replace("-", "").replace("+", "").isdigit() and
            (imaginary.replace("-", "").replace("+", "").isdigit() or
            (imaginary[-1] == 'i') and imaginary[:-1].replace("-", "").replace("+", "").replace("*", "").isdigit())):
            return True
        else:
            return False
    except ValueError:
        print("No me gusta ese imaginario")
        return False
