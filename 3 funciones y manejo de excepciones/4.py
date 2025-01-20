def factorial(n):
    if n < 1:
        return 1
    
    return n * factorial(n-1)

# print(factorial(5))

def fibonacci(n):
    if n==0:
        return 0
    
    if n==1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(3))

def sumatoria (n):
    """ n(n+1)/2 """
    
    if n==1:
        return 1
    return n + sumatoria(n-1)

print(sumatoria(10))
