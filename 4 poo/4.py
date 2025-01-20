""" 
concesionaria de vehiculos 
    Gestion de vehiculos
        Se podra hacer compra y venta
    Preguntar usuario
        Cuales son los que estan disponibles
        precio,
        compra
        
    clases
        user
            name
            age
            money = 0
            myCars = []
            
        Vehicle
            name
            brand
            price
            stock
            available()
            
        Dealership
            vehicles = []
            users = []
            
            available_vehicles()
            buy_vehicle()
            sell_vehicle()

"""
        
from typing import List
        
class Vehicle:
    def __init__(self, name:str, brand:str, price=0, stock=0):
        self.name = name
        self.brand = brand
        self.price = max(0, price)
        self.stock = max(0, stock)

    def available(self):
        return self.stock > 0

    def sale(self):
        if self.stock <= 0:
            print(f"[Vehicle] {self.name}, esta sin stock")
            self.stock = 0
            return

        self.stock -= 1
        print(f"[Vehicle] Se vendio {self.name}, el stock actual es {self.stock}")

    def buy(self, count = 1):
        self.stock += max(1, count)
        print(f"[Vehicle] Se compro {self.name}, el stock actual es {self.stock}")

class User:
    def __init__(self, name:str, age:int, money:float):
        self.name = name
        self.age = age
        self.money = money
        self.myCars: List[Vehicle] = []
        
    def buy_vehicle(self, vehicle:Vehicle):
        if vehicle in self.myCars:
            print(f"[User] {self.name}, El vehiculo {vehicle.name} ya lo compraste")
            return
        
        if not vehicle.available():
            print(f"[User] {self.name}, El vehiculo {vehicle.name} no esta disponible")
            return
        
        vehicle.sale()
        self.myCars.append(vehicle)
        print(f"[User] {self.name}, compro el vehiculo {vehicle.name}")
        
    def remove_vehicle(self, vehicle:Vehicle):
        if not vehicle in self.myCars:
            print(f"[User] {self.name}, No se puede desechar {vehicle.name} por que aun no lo tienes")
            return
        
        print(f"[User] {self.name}, Se desecho {vehicle.name}")
        self.myCars.remove(vehicle)

class Dealership:
    def __init__(self):
        self.vehicles: List[Vehicle] = []
        self.users: List[User] = []
        
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
        
    def add_user(self, user: User):
        self.users.append(user)
        
    def show_available_vehicles(self):
        print('[Dealership] Vehiculos disponibles:')
        for vehicle in self.vehicles:
            if vehicle.available():
                print(f"  {vehicle.brand}: {vehicle.name}")
                
    def buy_vehicle(self, vehicle: Vehicle, count = 1):
        if not vehicle in self.vehicles:
            print(f"[Dealership] No existe este vehiculo ${vehicle.name}")
            return
        
        vehicle.buy(count)
        print(f"[Dealership] Nuevo stock en la concesionaria del vehiculo {vehicle.name}, stock actual {vehicle.stock}")
        
vehiculo1 = Vehicle("Agya", "Toyota", 16182, 5)
vehiculo2 = Vehicle("Kona Hybrid", "Hyundai", 114342, 1)

usuario1 = User("Hanns", 22, 500000)

concesionaria = Dealership()

concesionaria.add_vehicle(vehiculo1)
concesionaria.add_vehicle(vehiculo2)

concesionaria.add_user(usuario1)

concesionaria.show_available_vehicles()
print()

usuario1.buy_vehicle(vehiculo1)
usuario1.buy_vehicle(vehiculo2)
print()

concesionaria.buy_vehicle(vehiculo1, 10)
concesionaria.buy_vehicle(vehiculo2, 10)
print()

usuario1.buy_vehicle(vehiculo2)
print()

usuario1.remove_vehicle(vehiculo2)
usuario1.buy_vehicle(vehiculo2)