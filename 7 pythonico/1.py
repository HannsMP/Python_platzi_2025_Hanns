from typing import List
def calculate_average(numbers:List[float|int]):
    """
    Calcula el promedio de una lista de numeros
    
    parametros:
        numbers: List[float|int]: una lista de numeros enteros o flotantes
        
    retorna:float
    """
    return sum(numbers) / len(numbers)

# imprimiento el resultado de la funcion
print(calculate_average([1, 2, 3, 4, 5])) # imprimiento el resultado de la funcion