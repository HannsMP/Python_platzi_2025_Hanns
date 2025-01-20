from typing import List

class Vehicle:
    def __init__(self, brand:str, model:str, price:float):
        self.is_available = True
        
        # Encapsulamiento
        self.brand = brand
        self.model = model
        self.price = price
        
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
            return
        
        print(f"El vehiculo {self.brand}. No esta disponible")
        
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price        
                
    def start_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')

        
    def stop_engine(self):
        raise NotImplementedError('Este metodo debe ser implementado por la subclase')
        
        
# Herencia
class Car(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"El coche {self.brand} no esta disponible"
        
        return f"EL motor del coche {self.brand} esta en marcha"
        
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"El coche {self.brand} no esta disponible"
        
        return f"EL motor del coche {self.brand} se a detenido"
    
# Herencia
class Bike(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"La bicicleta {self.brand} no esta disponible"
        
        return f"La bicicleta {self.brand} esta en marcha"
        
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"La bicicleta {self.brand} no esta disponible"
        
        return f"La bicicleta {self.brand} se a detenido"
    
# Herencia
class Truck(Vehicle):
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"El camion {self.brand} no esta disponible"
        
        return f"EL motor del camion {self.brand} esta en marcha"
        
    # Polimorfismo
    def start_engine(self):
        if self.check_available():
            return f"El camion {self.brand} no esta disponible"
        
        return f"EL motor del camion {self.brand} se a detenido"
    
class Customer:
    def __init__(self, name):
        self.purchased_vehicles = []
        
        # Encapsulamiento
        self.name = name
        
    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            return
        
        print(f"Lo siento, {vehicle.brand} no esta disponible")
        
    def inquire_vehicle(self, vehicle:Vehicle):
        availablity = vehicle.check_available if "Disponible" else "No disponible"
        
        print(f"El {vehicle.brand} este {availablity} y cuesta {vehicle.get_price()}")
        
class Dealership:
    def __init__(self):
        
        # Encapsulamiento
        self.inventory:List[Vehicle] = []
        self.customers:List[Customer] = []
        
    def add_vehicles(self, vehicle:Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")
        
    def register_customers(self, customer:Customer):
        self.customers.append(customer)
        print(f"El Cliente {customer.name} ha sido añadido")
        
    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")
                
# Herencia
# Abstraccion
# Encapsulamiento
# Polimorfismo

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

dealership.show_available_vehicle()

dealership.register_customers(customer1)
customer1.inquire_vehicle(car1)

customer1.buy_vehicle(car1)

dealership.show_available_vehicle()
