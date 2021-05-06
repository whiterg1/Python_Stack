class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account_balance}")
        return self
john = User("John Wick", "Babayaga1@gmail.com")
beatrix = User("Beatrix Kiddo", "The_bride@gmail.com")
thomas = User("Thomas Anderson", "The_one@gmail.com")

john.make_deposit(10).make_deposit(10).make_deposit(10).make_withdrawal(5).display_user_balance()
beatrix. make_deposit(20).make_deposit(30).make_withdrawal(10).make_withdrawal(15).display_user_balance()
thomas.make_deposit(100).make_withdrawal(25).make_withdrawal(25).make_withdrawal(25).display_user_balance()
