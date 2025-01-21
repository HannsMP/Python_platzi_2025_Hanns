""" 
Un metodo estatico para verificar si el monto de un pedido es mayor a un minimo permitido (
    por ejemplo 50 dolares
)

Un metodo de clase que permita crear un pedido aplicando un descuento global
"""

class Order:
    
    TAX_RATE = .18
    DISCOUNT_RATE = .05
    
    @staticmethod
    def check_valid_amount(amount:float|int):
        if not (isinstance(amount, float) or isinstance(amount, int)):
            raise TypeError("El parametro monto no es un numero")        
        return amount > 50
    
    @classmethod
    def apply_tax(cls, amoun:float):
        return amoun * cls.TAX_RATE
    
    @classmethod
    def apply_discount(cls, amoun:float):
        return amoun * cls.DISCOUNT_RATE
        
    @classmethod
    def create_order(cls, amount:float|int):
        is_valid_amount = cls.check_valid_amount(amount)
        
        # aplica un impuesto a todo
        amount_with_tax = amount + cls.apply_tax(amount)
        
        # si un un monto valido aplicara una tasa descuento
        if is_valid_amount:
            return amount_with_tax  - cls.apply_discount(amount)
        
        return amount_with_tax

    
print(Order.check_valid_amount(51))

print(Order.create_order(52)) # sin descuento 61.36, con descuento 58.76
print(Order.create_order(42)) # 49.56