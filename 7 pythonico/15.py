from collections import defaultdict, Counter, deque
from enum import Enum
    
class OrderStatus(Enum):
    PENDING = 1 # Pendiente
    SHIPPED = 2 # Enviado
    DELIVERED = 3 # Entregado
    
class Order:
    def __init__(self, name:str):
        self.name = name
        self.status = OrderStatus.PENDING
    
class Client:
    id_public = 1
    
    def __init__(self , name:str):
        self.name = name
        self.id = Client.id_public
        Client.id_public +=1
        
    def query_order(self, order):
        pass
    
class ControllerClient:
    def __init__(self):
        self.clients = defaultdict(Client)
    
    def add_client(self, client:Client):
        self.Clients[client.name] = Client
    
class ControllerOrder:
    def __init__(self):
        self.orders:defaultdict[str, int] = defaultdict(int)
        
    def add_product(self, name_product:str, count:int = 1):
        if not isinstance(count, int):
            raise TypeError("La cantidad debe ser un numero y entero")
        
        if count < 1:
            raise ValueError("La cantidad del producto debe ser positiva y no cero")
        
        self.orders[name_product] += count
        print(f"El producto: {name_product}, cantidad actual {self.orders[name_product]}.")
        
    def order_product(self, name_product:str, count:int = 1):
        if not isinstance(count, int):
            raise TypeError("La cantidad debe ser un numero y entero")
        
        if count < 1:
            raise ValueError("La cantidad del producto debe ser positiva y no cero")
        
        if self.orders[name_product] == 0:
            return False
        
        self.orders[name_product] -= count
        return True
    
    def show_product_available(self):
        keys = self.orders.keys()
        print(f"Productos disponibles")
        
        for key in keys:
            print(f"  {key}: {self.orders[key]}")
    
controlle = ControllerOrder()
    
cliente1 = Client("Max")
cliente2 = Client("Junior")

