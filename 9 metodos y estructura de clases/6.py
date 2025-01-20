""" 
crear una funcion que reciba una cantidad variable de productosy sus precios.
calcule el total y aqplique un descuento opcional si se proporciona como un argumento con nombre

usar args para recibir una lista de precios

usar kwargs para aceptar un descuento opcinal y aplicarlo al total

"""

def proccess_products(*products, **data):
    total = sum(products)
    return total - data.get('descuento', 0)

print(proccess_products(12, 23, 34, 45, 56, 67, 78, 89, descuento=16))