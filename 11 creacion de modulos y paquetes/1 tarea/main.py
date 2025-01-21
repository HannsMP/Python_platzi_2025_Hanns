months = [
    {
        "name": "Enero",
        "income": 2000,
        "expenses": 1800
    },
    {
        "name": "Febrero",
        "income": 2200,
        "expenses": 2300
    },
    {
        "name": "Marzo",
        "income": 2100,
        "expenses": 1950
    },
    {
        "name": "Abril",
        "income": 2500,
        "expenses": 2600
    },
    {
        "name": "Mayo",
        "income": 2300,
        "expenses": 2200
    },
    {
        "name": "Junio",
        "income": 2400,
        "expenses": 2500
    },
    {
        "name": "Julio",
        "income": 2600,
        "expenses": 2400
    },
    {
        "name": "Agosto",
        "income": 2700,
        "expenses": 2750
    },
    {
        "name": "Septiembre",
        "income": 2800,
        "expenses": 2900
    },
    {
        "name": "Octubre",
        "income": 3000,
        "expenses": 2850
    },
    {
        "name": "Noviembre",
        "income": 3200,
        "expenses": 3100
    },
    {
        "name": "Diciembre",
        "income": 3300,
        "expenses": 3400
    }
]
from mod import calculate_balance, profitable_banlace

for month in months:
    balance = calculate_balance(month["income"], month["expenses"])
    
    if profitable_banlace(balance):
        print(f"Balance rentable para el mes de {month['name']}: {balance}")
    else:
        print(f"  No rentable para el mes de {month['name']}: {balance}")            