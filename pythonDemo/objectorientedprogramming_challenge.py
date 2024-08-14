class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposited):
        self.balance += deposited
        print(f"This is now your new balance: {self.balance}")



    def withdraw(self, cashout):
        if cashout < self.balance:
            self.balance -= cashout
            print(f"This is now your new balance: {self.balance}")
        else:
            print("You do not have enough balance to withdraw that amount. \n"
                  f"This is your current balance {self.balance}")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


my_account = Account("Matt", 10000)
my_account.withdraw(8000)
my_account.deposit(1000)
my_account.withdraw(7000)
print(my_account)
