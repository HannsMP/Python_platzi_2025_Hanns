"""
1. La funcion recibira una lista de diccionarios. Cada diccionario tendra las claves: "name", "age", "salary".
2. La funcion debe devolver una lista de empleados que ganen mas de un cierto sueldo.
"""

# lista generada por chatgpt, si quieres copiala
employees = [
  { "name": "Alice", "age": 30, "salary": 55000 },
  { "name": "Bob", "age": 25, "salary": 45000 },
  { "name": "Charlie", "age": 35, "salary": 60000 },
  { "name": "Diana", "age": 28, "salary": 48000 },
  { "name": "Eve", "age": 32, "salary": 53000 },
  { "name": "Frank", "age": 29, "salary": 47000 },
  { "name": "Grace", "age": 27, "salary": 46000 },
  { "name": "Hank", "age": 33, "salary": 52000 },
  { "name": "Ivy", "age": 26, "salary": 44000 },
  { "name": "Jack", "age": 31, "salary": 51000 }
]

def filter_employees (amount: int|float) -> list[dict[str, str|int|float]]:
    if amount<0:
        raise Exception("No existe el monto o no es valido para el filtrado")
    return [employee for employee in employees if employee["salary"] > amount]

print(filter_employees(50000))