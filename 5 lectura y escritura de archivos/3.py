import csv

file_path = 'csv/products.csv'
updated_file_path = 'csv/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    fieldnames = csv_reader.fieldnames + ['total_value']
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_write = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_write.writeheader()
        
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_write.writerow(row)