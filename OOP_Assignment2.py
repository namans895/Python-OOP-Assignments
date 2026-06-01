# Bank Account System using Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


# Creating object
acc = BankAccount(5000)

acc.deposit(2000)
acc.withdraw(1000)

print("Current Balance :", acc.get_balance())
