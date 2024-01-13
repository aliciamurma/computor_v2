import re
from aux import *
from library import *

def ft_ask_value(var):
    var2 = var.split('=')
    if len(var2) != 2:
        print("Error in syntax 1")
        return (False)
    part = var2[1].strip()
    if len(part) == 1 and part == "?":
        return True
    return False

def ft_separate(var):
    pattern = r'\b\w+\b|[()+\-^*/%]'
    matches = re.findall(pattern, var)
    output_str = ' '.join(matches)
    return output_str

def ft_print_asked(var):
    var2 = var.split('=')
    asked = var2[0].strip()
    separated = ft_separate(asked)
    replaced = ft_replace_variables(separated)
    if ft_is_rational_number(replaced):
        print ("rational")
    print(replaced)
