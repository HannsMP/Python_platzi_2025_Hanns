""" 
impletar un sistema de descarga de archivos asincrona,
donde cada archivo tarde un tiempo variable en descargarse
"""

from multiprocessing import Pool
from time import sleep
from random import randint

def download_file(name:str):
    time = randint(1, 10)
    print(f"Se inicio la descarga del archivo {name}\n tiempo de espera de {time} segundos")
    sleep(time)
    print(f"Descarga finalizada {name}")

if __name__ == '__main__':
    
    files = ['Pokemon_rubi_omega.3ds', 'Valorant.exe', 'Genshin_impact.exe', 'Mario_bros.gba']

    with Pool() as pool:
        pool.map(download_file, files)
        