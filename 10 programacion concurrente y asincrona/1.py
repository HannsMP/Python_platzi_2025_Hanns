""" 
# concurrencia 
definicion: 
    Manejo de multiples tareas progresivamente
usos ideales:
    Operaciones I/O (espera de red, escritura de archivos)
implementacion
    threading, asyncio
"""


from threading import Thread
from time import sleep

def process_request(request_id:int, ):
    print(f"Procesanso solicitud {request_id}")
    sleep(3)
    print(f"Solicitud {request_id}, completada")
    
threads:list[Thread] = []

for i in range(3):
    # crear nuevo hilo que ejecutara la funcion
    thread = Thread(target=process_request, args=(i,))
    
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("todas las solicitudes completadas")