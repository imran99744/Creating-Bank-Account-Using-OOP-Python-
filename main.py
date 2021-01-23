class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def print_balance(self):
        return self.balance


account = BankAccount()
account.deposit(100)
account.deposit(50)
account.deposit(200)

print(account.print_balance())
