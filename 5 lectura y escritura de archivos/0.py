# leer un archivo linea por linea
with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())

# leer todas las linaas en una lista
with open('caperucita.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas.strip())

# agregar al final
with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")
    
# sobreescribir el contenido del archivo
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")
    
with open('caperucita.txt', 'r') as file:
    lineas = file.readlines()
    print(len(lineas))