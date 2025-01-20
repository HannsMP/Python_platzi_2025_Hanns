# 1. Funcione para agregar empleados y eliminar empleados de una lista
# 2. un bloque if __name__ == '__main__': Que permita probar el funcionamiento del script ejecutandolo directamente.

from enum import Enum

class AccessError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Rols(Enum):
    ADMIN = 1
    EMPLOYEE = 2

class User:
    def __init__(self, name:str, rol:Rols):
        self.name = name
        self.rol = rol

def loggue(message_append:str):
    with open('log/action.log', 'a') as file:
        file.write('\n' + message_append)

def log_action (accion):
    def decorator(func):
        def wrapper(this, user:User):
            try:
                res = func(this, user)
                loggue(f"[Accion] (user: {user.name}, rol: {user.rol}, accion: {accion})")
                return res
            except AccessError as err:
                loggue(f"[AccessError] (user: {user.name}, rol: {user.rol}, accion: {accion}), {err}")
                raise err
            except TypeError as err:
                loggue(f"[TypeError] (user: {user.name}, rol: {user.rol}, accion: {accion}), {err}")
                raise err
            except Exception as err:
                loggue(f"[Error] (user: {user.name}, rol: {user.rol}, accion: {accion}), {err}")
                raise err
            
        return wrapper
    return decorator
       
def check_access (require_rol:Rols, accion:str):
    def decorator(func):
        @log_action(accion)
        def wrapper(this, user:User):
            if not isinstance(user, User):
                raise TypeError(f"El parametro user es para un usuario con la instancia User")
            
            if user.rol != require_rol:
                raise AccessError(f"El usario {user.name} intento pero no tienes permisos para {accion} usuarios")
        
            return func(this, user)
        
        return wrapper
    return decorator
 
class Handle_User:
    data = []
    
    @check_access(Rols.ADMIN, "agregar")
    def add (self, user:User):
        if user in self.data:
            return False
        
        self.data.append(user)
        return True
        
    @check_access(Rols.ADMIN, "eliminar")
    def remove(self, user:User):
        if not user in self.data:
            return False
        
        self.data.remove(user)
        return True
    

# pruebas
if __name__ == '__main__':
    try:
        empleado1 = User("Maria", Rols.ADMIN)
        empleado2 = User("Jose", Rols.EMPLOYEE)
        
        handle = Handle_User()
        print('1', handle.add(empleado1))
        print('1', handle.add(empleado1))
        
        # print('2', handle.remove(empleado2))
        # print('2', handle.add(empleado2))
        
        print('1', handle.remove(empleado1))
        # print('2', handle.remove(empleado2))
    except AccessError as e:
        print(e)