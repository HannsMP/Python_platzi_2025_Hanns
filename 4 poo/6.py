class LivingBeging:
    def __init__(self, name:str):
        self.name = name
class Person(LivingBeging):
    def __init__(self, name:str, age:int):
        super().__init__(name)
        self.age = age
        
    def greet(self):
        print("Hello! I am a person.")
        
class Student(Person):
    def __init__(self, name:str, age:float, student_id:str):
        super().__init__(name, age)
        self.student_id = student_id
        
    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")
    
    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"    
    
student = Student("Ana", 20, "S123")
student.greet()

print(student)
print(repr(student))

# Importancia de Aprender estos Conceptos
# Comprender y utilizar super(), los métodos por defecto y los constructores es crucial para escribir código limpio, eficiente y reutilizable en Python. Estos conceptos permiten:

# Extender Funcionalidades: super() permite extender las funcionalidades de una superclase sin duplicar código.
# Inicialización Correcta: El uso adecuado de constructores asegura que todos los atributos sean inicializados correctamente.
# Personalizar Representaciones: Métodos como __str__ y __repr__ permiten personalizar cómo se representan los objetos, facilitando la depuración y el manejo de datos.
# Comparar y Ordenar Objetos: Métodos como __eq__, __lt__, etc., permiten definir cómo se comparan y ordenan los objetos, lo cual es esencial para muchas operaciones de datos.