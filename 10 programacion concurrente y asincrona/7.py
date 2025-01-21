""" 
Division de tareas

    verificacion de inventario
    calculo de costo total
    procesamiento de pago
"""

import asyncio
import time
import random
import multiprocessing

# verificar el inventario
async def check_inventory(item):
    print(f"Verificando el inventario para {item}...")
    await asyncio.sleep(random.randint(3, 6))
    print(f"  Inventario verificado para {item}")
    
    return random.choice([True, False])

# procesamiento de pago
async def process_payment(order_id):
    print(f"Procesando pago para la orden {order_id}...")
    
    await asyncio.sleep(random.randint(3, 6))
    print(f"Pago procesado para la orden {order_id}")
    
    return True

def calculate_total(items):
    print(f"Calculando el costo total para el {len(items)} articulos")
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f"Costo total: {total}")
    return total

async def process_order(order_id, items):
    print(f"Iniciando el procesamiento de la orden {order_id}...")
    
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)
    
    if not all(inventory_results):
        print(f"La orden {order_id} cancelada, producto no disponible")
        
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))
        
    payment_result = await process_payment(order_id)
    
    if payment_result:
        print(f"  La orden {order_id} completada con exito. Total: {total}")
        
    else:
        print(f"  Error al procesar el pago de la orden {order_id}")
        
async def main():
    orders = [
        {
            "id":1, "items": [
                {"name": 'Laptop', "price": 1000},
                {"name": 'Mouse', "price": 50},
            ],
            "id":2, "items": [
                {"name": 'Teclado', "price": 80},
                {"name": 'Monitor', "price": 300},
            ],
            "id":3, "items": [
                {"name": 'Smartphone', "price": 700},
                {"name": 'Funda', "price": 20},
            ]
        }
    ]
    
    # procesar multiples ordenes, cocurrentemente
    
    task = [process_order(order['id'], order["items"]) for order in orders]
    await asyncio.gather(*task)
    
if __name__ == '__main__':
    asyncio.run(main())