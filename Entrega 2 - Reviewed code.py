from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def bank_name(self):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

class Account(Bank):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def bank_name(self):
        return "MyBank"

    def transfer(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Money transferred successfully")
            print("New balance is {}".format(self.balance))

class ATM(Bank):
    def __init__(self, location, bank_name):
        self.location = location
        self.bank_name = bank_name

    def bank_name(self):
        return self.bank_name

    def transfer(self, amount, account):
        if amount > 0:
            account.transfer(amount)
        else:
            print("Invalid amount for transfer, value has to be greater than 0")

# Create an Account instance
account1 = Account("Luis", 10000)

# Create an ATM instance
ATM1 = ATM("Laureles", "Bancolombia")

# Transfer money from the ATM to the account
ATM1.transfer(500, account1)

