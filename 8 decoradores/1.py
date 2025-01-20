def log_transaction(func):
    def wrapper():
        print('Log de la transaccion...')
        
        func()
        
    return wrapper

@log_transaction
def process_payment():
    print('Procesando pago...')