c_real = 0
c_imag = 0

variables = {}

# Creamos un diccionario
class MyVar:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Necesitamos que sean strings, si no printa la dirección de memoria
    def __str__(self):
        return f"MyVar(name={self.name}, value={self.value})"