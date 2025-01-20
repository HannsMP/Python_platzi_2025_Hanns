from collections import defaultdict

def count_products(orders:list[str]) -> defaultdict:
    product_count = defaultdict(int) # valor por defecto: 0
    
    for product in orders:
        product_count[product]+=1
        
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)