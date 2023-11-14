
def ft_is_variable(var):
    var2 = var.split('=')
    if len(var2) == 2:
        return (True)
    return (False)

def ft_find_variable(dictionary, name):
    print("Im HERE")
    for clave, value in dictionary.items():
        print("The names are: ", value.name)
        if value is not None:  # Check if value is not None before accessing its attributes
            if value.name == name:
                return value  # Retorna la instancia de MyVar si se encuentra el nombre
    return None 
