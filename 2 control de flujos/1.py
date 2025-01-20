# comprehesions list
squares = [x**2 for x in range(1,11)]

print(squares)

celsius = [0,10,20,30,40]

fahrenheit = [ (t * 9/5) * 32 for t in celsius ]

print(fahrenheit)

pares = [ x for x in range(1,21) if x%2 == 0 ]

print(pares)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transposed = [
    [row[i] for row in matrix]
        for i in range(len(matrix[0]))
]

print(transposed)

# equivalente a

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    
    for row in matrix:
        transposed_row.append(row[i])
        
    transposed.append(transposed_row)
    
print(transposed)