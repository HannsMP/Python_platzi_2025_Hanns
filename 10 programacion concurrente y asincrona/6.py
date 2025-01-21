""" 
impletar un sistema de descarga de archivos asincrona,
donde cada archivo tarde un tiempo variable en descargarse
"""

import asyncio
import time
from random import randint

async def download_file(name:str, delay:int):
    await asyncio.sleep(delay)
    
    async_time = randint(1, 10)
    print(f"Se inicio la descarga del archivo {name}\n tiempo de espera de {async_time} segundos")
    
    await asyncio.sleep(async_time)
    print(f"Descarga finalizada {name}")

files = [
    {
        "name": 'Pokemon_rubi_omega.3ds', 
        "time_delay": 2
    }, 
    {
        "name": 'Valorant.exe', 
        "time_delay": 3
    }, 
    {
        "name": 'Genshin_impact.exe', 
        "time_delay": 4
    }, 
    {
        "name": 'Mario_bros.gba', 
        "time_delay": 1
    }
]

async def main():    
    for file in files:
        await download_file(file["name"], file["time_delay"])
        
asyncio.run(main())