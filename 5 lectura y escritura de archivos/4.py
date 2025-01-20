from typing import List, Dict
import json

new_data =     {
    "name": "Wireless Chatger",
    "price": "75",
    "quantity": "100",
    "brand": "chargerMaster",
    "category": "Accessories",
    "entry_date": "2024-07-01"
}

file_path = 'json/products.json'
with open(file_path, 'r') as file:
    products:List[Dict] = json.load(file)
    
products.append(new_data)

with open(file_path, 'w') as file:
    json.dump(products, file, indent=4)