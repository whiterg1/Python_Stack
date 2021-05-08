class BankAccount:
    bank_name = "The National Bank of Roy"
    all_accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f' This account has a balance of: ${self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.int_rate * self.balance 
            return self
        else:
            print("There are insufficient funds in the account.")

bubbas_bbq = BankAccount(0.03, 0)
ginos_barbershop = BankAccount(0.06, 0)

bubbas_bbq.deposit(30).deposit(50).deposit(10).withdraw(20).yield_interest().display_account_info()
ginos_barbershop.deposit(200).deposit(50).withdraw(100).withdraw(10).withdraw(10).withdraw(20).yield_interest().display_account_info()