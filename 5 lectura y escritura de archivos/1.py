import csv

# lectura por filas
with open('csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
        
# lectura por columnas
with open('csv/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Prodcuto: {row['name']}, Precio: {row['price']}")