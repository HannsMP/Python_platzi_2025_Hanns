class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"Persona: {self.nombre}, {self.edad} años"
    
    def __repr__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad='{self.edad}')"

    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __ne__(self, otra_persona):
        return self.nombre != otra_persona.nombre and self.edad != otra_persona.edad

    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

    def __le__(self, otra_persona):
        return self.edad <= otra_persona.edad

    def __gt__(self, otra_persona):
        return self.edad > otra_persona.edad
    
    def __ge__(self, otra_persona):
        return self.edad >= otra_persona.edad
    
    def __add__(self, otra_persona):
         return self.edad + otra_persona.edad
     
     
p1 = Persona("Ana", 28)
p2 = Persona("Luis", 35)
p3 = Persona("Ana", 28)

print(p1)

print(repr(p1))

print(p1 == p3)

print(p1 < p2) # lt
print(p1 <= p2) # le
print(p1 > p2) # gt
print(p1 >= p2) # ge

print(p1 + p2)