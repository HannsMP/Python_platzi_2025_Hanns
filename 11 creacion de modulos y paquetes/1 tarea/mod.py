def calculate_balance(income:float|int, expenses:float|int) -> float|int:
    return income - expenses

def profitable_banlace(balance:float|int) -> bool:
    return balance > 0