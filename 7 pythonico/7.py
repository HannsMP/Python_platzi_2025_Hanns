id1:int = 101
id2:int = 102

total_id:int = id1 + id2

print(total_id)

def add_employee_ids(id1:int, id2:int) -> int:
    return id1 + id2

print(add_employee_ids(101, 102))

class Employee:
    name:str
    age:int
    salary:float
    
    def __init__(self, name:str, age:int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary
        
    def introduce(self) -> str:
        return f"Hola, me llamo {self.name}, tengo {self.age}"
    
employee1 = Employee('carlos', 30, 3500.)

print(employee1.introduce())

# pip install mypy 
# import optional, union

# int 
# float
# str
# bool
# list
# dict
# tuple
# ...