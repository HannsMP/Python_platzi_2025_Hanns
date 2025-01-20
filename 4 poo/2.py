class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposit (self, amount):
        if not self.is_active:
            print(f"No se puede depositar {amount}, cuenta inactiva")
            return 
        
        self.balance += amount
        print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        
    def withdraw(self, amount):
        if not self.is_active:
            print(f"No se puede retirar {amount}, cuenta inactiva")
            return
         
        if amount > self.balance:
            print("no tienes suficiente para retirar")
            return
        
        self.balance -= amount
        print(f"Se ha retirado {amount}. Saldo actual {self.balance}")
        
    def deactive_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")
        
    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")
        
account1 = BankAccount("Hanns", 500)
account2 = BankAccount("Neyer", 1000)

account1.deposit(200)
account2.deposit(100)

account1.deactive_account()
account1.deposit(50)

account1.activate_account()
account1.deposit(50)