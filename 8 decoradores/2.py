def check_access(require_rol):
    def decorador(func):
        def wrapper( employee):
            if(employee.get('rol')) == require_rol:
                return func(employee)
            else:
                print(f"Acesso denegado")
                
        return wrapper
    return decorador

def log_action(func):
    def warpper(employee):
        print(f"registrando accion para el empleado {employee['name']}")
        return func(employee)
        
    return warpper

@check_access('admin')
@log_action
def delete_employee(employee):
    print(f"El empleado {employee['name']}, ha sido elminiado")
    
admin = {'name': 'carlos', 'rol': 'admin'}
employee = {'name': 'Ana', 'rol': 'employee'}

delete_employee(admin)