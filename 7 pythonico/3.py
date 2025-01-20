### inner y outer

x = 'global'

# Funcion externa
def outer():
    x = 'enclosing'
    
    # Funcion interna
    def inner():
        x = 'local'
        print(x)
        
    inner()
    print(x)
    
outer()
print(x)