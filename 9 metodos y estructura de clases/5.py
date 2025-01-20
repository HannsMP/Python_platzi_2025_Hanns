#  *args, *kwargs

class Employee:
    def __init__(self, name, *arg, **kwargs):
        self.name = name
        self.skills = arg
        self.details = kwargs
    
    def show(self):
        print(f"Employee: {self.name}")
        print('Skills', self.skills)
        print('Details', self.details)
        
employee = Employee('Carlos', 'Python', 'Java', 'C++', age=22, city="Lima")
employee.show()