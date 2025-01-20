import csv, json

with open('csv/products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    data = []
    
    for row in csv_reader:
        data.append(row)
        
    data_str = json.dumps(data)
        
    with open('json/csv_products.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    