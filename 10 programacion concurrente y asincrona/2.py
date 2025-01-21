""" 
# paralelismo 
definicion: 
    Ejecucion simultanea de multiples tareas
usos ideales:
    Tareas que requiren mucho calculo
implementacion
    multiprocessing
"""
from multiprocessing import Pool

# funcion que calcule el cuadrado de un numero 
def calculate_square(n):
    return n*n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    
    with Pool() as pool:
        results = pool.map(calculate_square, numbers)
        
    print(f"resultados: {results}")