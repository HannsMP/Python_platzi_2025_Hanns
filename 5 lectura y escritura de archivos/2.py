import csv

new_product = {
    'name': "Wireless Chatger",
    'price': 75,
    'quantity': 100,
    'brand': "chargerMaster",
    'category': "Accessories",
    'entry_date': "2024-07-01"
}

with open('csv/products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_write = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_write.writerow(new_product)