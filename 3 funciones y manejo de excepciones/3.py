add = lambda a,b: a + b

print(add(10,4))

mul = lambda a,b: a*b

numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)

even_numbers = list(filter(lambda x:x%2 == 0, numbers))

print(even_numbers)