def reduce (list:list[float|int], func, init_value=0) -> float|int:
    for current_value in list:
        init_value = func(init_value, current_value)
        
    return init_value

def addition (*values:float|int):
    return reduce(values, lambda acumulador, actual: acumulador + actual, 0)

def subtraction (*values:float|int):
    return reduce(values, lambda acumulador, actual: acumulador - actual, 0)

def division (*values:float|int):
    if len(values) == 0:
        raise ValueError("Debe proporcionar al menos un valor.")
    if 0 in values[1:]:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return reduce(values[1:], lambda acumulador, actual: acumulador / actual, values[0])

def multiplication (*values:float|int):
    if 0 in values:
        return 0
    return reduce(values, lambda acumulador, actual: acumulador * actual, 1)

if __name__ == '__main__':
    print(addition(4, 4, 4, 4))
    print(subtraction(10, 4, 6))
    print(division(12, 3))
    print(multiplication(2, 5, 7))