def generator():
    yield 1
    yield 2
    yield 3
    
for value in generator():
    print(value)
    
    
def fibinacci(limit):
    a, b = 0, 1
    
    while(a < limit):
        yield a
        
        a, b = b, a+b
        
for num in fibinacci(10):
    print(num)