# SintaxError
# TypeError
# ZeroDivisionError

try:
    divisor = float(input('Ingresa un numero divisor: '))
    result = 100/divisor
    print(result)
    
except ZeroDivisionError as e:
    print('Error: El divisor no puede ser cero')
    print(e)
    
except ValueError as g:
    print('Error: Debes introducir un numero valido')
    print(g)