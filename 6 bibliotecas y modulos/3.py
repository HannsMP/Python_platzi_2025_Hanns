import statistics
import csv

monthly_sales = {}

with open('csv/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales =  int(row['sales'])
        monthly_sales[month] = sales
        
sales = list(monthly_sales.values())

# hallar media
mean_sales = statistics.mean(sales)
print(f"La media es {mean_sales}")

# hallar mediana
median_sales = statistics.median(sales)
print(f"La mediana es {median_sales}")

# hallar moda
mode_sales = statistics.mode(sales)
print(f"La moda es {mode_sales}")

# hallar desviacion estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviacion estandar es {stdev_sales}")

# hallar varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es {variance_sales}")

max_sales = max(sales)
print(f"El maximo es {max_sales}")

min_sales = min(sales)
print(f"El minimo es {min_sales}")

range_sales = max_sales - min_sales
print(f"rango de ventas es {range_sales}")