def mi_decorador(funcion):
    def nueva_funcion(parametro):
        print("Antes de ejecutar la funcion")
        
        funcion(parametro)
        
        print("Despues de ejecutar la funcion")
        
    return nueva_funcion


#####################################################


@mi_decorador
def mi_funcion(parametro):
    print(f"Ejecutando la funcion con el parametro: {parametro}")
    
    

mi_funcion("Ejemplo")