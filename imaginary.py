from library import *

def ft_save_imaginary(var):
    print("Save imaginary")

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