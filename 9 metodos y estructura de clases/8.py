""" 
    gestion de perdidos
informacion de pedidos
calcular impuestos
gestionar datos

- static method
- class method

"""

class Order:
    gloabal_dismount = 10
    
    def __init__(self, amount:float):
        self.amount = amount
        
    @classmethod
    def update_gloabal_discount(cls, new_discount):
        cls.gloabal_dismount = new_discount

    @staticmethod
    def caculate_tax(amount:float, tax_rate:float):
        """ 
        calcula el impuesto relativo a un porsentaje
        amount:floar, monto a calcular
        tax_rate:float, valor entre 0 y 1
        """
        return amount* tax_rate
    
print(Order.caculate_tax(1000, .4))

Order.update_gloabal_discount(15)

print(Order.gloabal_dismount)