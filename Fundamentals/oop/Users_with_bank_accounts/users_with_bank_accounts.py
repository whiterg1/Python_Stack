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

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(0.01, 0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

john = User("John Wick", "Babayaga1@gmail.com")
beatrix = User("Beatrix Kiddo", "The_bride@gmail.com")
thomas = User("Thomas Anderson", "The_one@gmail.com")

john.account.deposit(15).display_account_info()
