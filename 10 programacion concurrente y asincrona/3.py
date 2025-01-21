"""
Uso de threading y multiprocessing en Python

DALLE_2024-10-16_17.25.15_-_A_rectangular_image_representing_threads_and_multi-processing_in_Python.The_image_should_feature_a_visual_metaphor_of_a_computers_CPU_with_multiple.jpg

Imagina que estás trabajando en una aplicación que necesita 
procesar múltiples tareas al mismo tiempo: desde manejar 
solicitudes web hasta realizar cálculos complejos de manera 
simultánea. A medida que las aplicaciones se vuelven más 
exigentes, las soluciones básicas de concurrencia ya no son 
suficientes. Aquí es donde entran las herramientas avanzadas 
de Python como threading y multiprocessing, que te permiten 
sacar el máximo provecho de tu CPU y gestionar tareas de 
manera eficiente y sin errores.

En esta clase, aprenderás a manejar escenarios más complicados, 
como evitar que los hilos interfieran entre sí, compartir 
datos de manera segura entre procesos y prevenir bloqueos que 
puedan detener tu aplicación. Prepárate para llevar la 
programación concurrente y paralela a un nivel más profesional 
y resolver problemas que los desarrolladores enfrentan en 
proyectos del mundo real.

1. Sincronización de Hilos en Python
Cuando varios hilos intentan acceder a un mismo recurso al 
mismo tiempo, pueden ocurrir problemas de coherencia. Para 
evitar esto, se utilizan mecanismos de sincronización, como 
Lock y RLock, que garantizan que solo un hilo acceda a un 
recurso crítico a la vez.

Ejemplo: Uso de Lock para Evitar Condiciones de Carrera
"""
import threading
# Variable compartida
saldo = 0
lock = threading.Lock()  # Crear un Lock

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # Bloquear el acceso para evitar condiciones de carrera
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}")  # Esperamos ver 200000 como saldo
"""
Explicación:

El uso de Lock asegura que solo un hilo modifique la variable 
saldo en un momento dado, evitando que el resultado final sea 
incorrecto.
2. Compartir Datos entre Procesos con multiprocessing
A diferencia de los hilos, los procesos no comparten memoria 
de forma predeterminada. Para que dos procesos puedan 
compartir datos, Python proporciona herramientas como 
multiprocessing.Queue y multiprocessing.Value.

Ejemplo: Compartir Datos con Queue en multiprocessing
"""
import multiprocessing
def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    cola = multiprocessing.Queue()

    proceso = multiprocessing.Process(target=calcular_cuadrado, args=(numeros, cola))
    proceso.start()
    proceso.join()

    # Extraer resultados de la cola
    while not cola.empty():
        print(cola.get())
"""
Explicación:

Usamos Queue para que el proceso secundario pueda pasar datos 
de vuelta al proceso principal.
3. Problemas de Sincronización y Cómo Evitarlos
A medida que manejas tareas más complejas, es posible que te 
encuentres con problemas como deadlocks y race conditions. 
Entender estos problemas es crucial para escribir código 
concurrente robusto.

Evitar Deadlocks con RLock
Un deadlock ocurre cuando dos o más hilos se bloquean 
mutuamente al esperar por un recurso que está siendo 
utilizado por otro hilo. Para evitar esto, podemos usar RLock 
en lugar de Lock.

Ejemplo: Uso de RLock para Evitar Deadlocks
"""
import threading

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.lock = threading.RLock()

    def transferir(self, otra_cuenta, cantidad):
        with self.lock:
            self.saldo -= cantidad
            otra_cuenta.depositar(cantidad)

    def depositar(self, cantidad):
        with self.lock:
            self.saldo += cantidad

cuenta1 = CuentaBancaria(500)
cuenta2 = CuentaBancaria(300)

hilo1 = threading.Thread(target=cuenta1.transferir, args=(cuenta2, 200))
hilo2 = threading.Thread(target=cuenta2.transferir, args=(cuenta1, 100))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Saldo cuenta1: {cuenta1.saldo}")
print(f"Saldo cuenta2: {cuenta2.saldo}")
"""
Explicación:

Usamos RLock para evitar que múltiples operaciones simultáneas 
en una cuenta causen bloqueos.
4. Coordinación de Tareas con multiprocessing.Manager
Cuando los procesos deben compartir estructuras de datos 
complejas (como listas o diccionarios), podemos usar un 
Manager para crear un espacio de memoria compartido entre 
procesos.

Ejemplo: Uso de Manager para Compartir Listas entre Procesos
"""
import multiprocessing

def agregar_valores(lista_compartida):
    for i in range(5):
        lista_compartida.append(i)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        lista_compartida = manager.list()

        proceso1 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))
        proceso2 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))

        proceso1.start()
        proceso2.start()

        proceso1.join()
        proceso2.join()

        print(f"Lista compartida: {lista_compartida}")
"""
Explicación:

multiprocessing.Manager nos permite crear una lista compartida 
entre varios procesos, facilitando la comunicación entre ellos.
¡Lo lograste! Ahora tienes en tus manos poderosas técnicas 
para manejar múltiples tareas de forma eficiente. Aprendiste 
a sincronizar hilos para evitar errores, a compartir datos de 
manera segura entre procesos y a evitar bloqueos que podrían 
detener tus aplicaciones. Todo esto te prepara para enfrentar 
los desafíos del desarrollo de software moderno, donde la 
concurrencia y el paralelismo son esenciales para crear 
aplicaciones rápidas, eficientes y escalables.

Con estas herramientas avanzadas, tu código no solo será más 
rápido, sino también más robusto y confiable. Este es el tipo 
de conocimiento que te permite destacar en proyectos grandes y 
complejos. ¡Estás listo para aplicar todo lo que has aprendido 
y optimizar tus próximas creaciones en Python!
"""