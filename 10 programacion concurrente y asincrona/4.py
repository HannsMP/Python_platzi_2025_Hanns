# corrutinas y asyncio

import asyncio

async def process_data(data):
    print(f"Procesando {data}...")
    #simular una operacion
    
    await asyncio.sleep(10)
    
    print(f"{data} procesada")
    
    return data * 2

async def main():
    print("inicio de procesamiento")
    result = await process_data('archivo.txt')
    
    print(f"resultado: {result}")
    
asyncio.run(main())