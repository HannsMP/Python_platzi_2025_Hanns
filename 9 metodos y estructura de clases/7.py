class Employee:
    def __init__(self):
        self._salary = 0
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value
    
    @salary.deleter
    def salary(self):
        del self._salary
      
      
employee = Employee()

employee.salary = 12

print(employee.salary)

del employee.salary