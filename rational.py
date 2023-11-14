def ft_save_rational(var):
    print("Save rational")

def ft_is_rational_numer(var):
    print("Inside is rational")
    var2 = var.split('=')
    if len(var2) != 2:
        return (False)
    right_side = var2[1].strip()  # Elimina espacios en blanco alrededor
    if right_side.isdigit():
        return (True)
    return (False)