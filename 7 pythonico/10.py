def divide(a:int, b:int) -> float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros.')
    
    if b==0:
        raise ValueError('El divisor no puede ser cero.')
    
    return a/b

try:
    res = divide(10, 0)
    print(res)
except Exception as e:
    print(f'Error: {e}')