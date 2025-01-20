x = 100

def local_function():
    x = 10
    print(f"El valor de la variable es {x}")
    
def show_global():
    print(f"El valor de la variable es {x}")
    
local_function()
# print(x) # NameError: name 'x' is not defined