def greet(name, lastname = "-"):
    print('hola', name, lastname)
    
greet('hanns')
greet('hanns', 'Maza')
greet(lastname='Maza', name='hanns')