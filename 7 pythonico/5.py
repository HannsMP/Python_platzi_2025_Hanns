def outer():
    x = 'enclosing'
    
    def inner():
        nonlocal x
        x = 'modified'
        print(f"El valor de inner es: {x}")
        
    inner()
    print(f"El valor outer: {x}")
    
outer()