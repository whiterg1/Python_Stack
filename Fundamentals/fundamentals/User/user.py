class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account_balance}")
john = User("John Wick", "Babayaga1@gmail.com")
beatrix = User("Beatrix Kiddo", "The_bride@gmail.com")
thomas = User("Thomas Anderson", "The_one@gmail.com")

john.make_deposit(10)
john.make_deposit(10)
john.make_deposit(10)
john.make_withdrawal(10)
john.display_user_balance()
beatrix. make_deposit(20)
beatrix.make_deposit(30)
beatrix.make_withdrawal(10)
beatrix.make_withdrawal(15)
beatrix.display_user_balance()
thomas.make_deposit(100)
thomas.make_withdrawal(25)
thomas.make_withdrawal(25)
thomas.make_withdrawal(25)
thomas.display_user_balance()

