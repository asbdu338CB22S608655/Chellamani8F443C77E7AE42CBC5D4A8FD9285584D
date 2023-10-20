class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to deposit & withdrawal machine")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nAmount Withdrawn: ", amount)
        else:
            print("\nInsufficient balance")

    def display(self):
        print("\nAccount Balance =", self.balance)

s = BankAccount()
s.deposit()
s.withdraw()
s.display()
print("\nThank you for using our services")