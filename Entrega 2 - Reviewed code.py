from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def bank_name(self):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

class Account(Bank):
    def __init__(self, owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        self.bank_name = "MyBank"  # Set the bank name here or remove it if not needed
    
    def bank_name(self):
        return super().bank_name()
    
    
    def transfer(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Transferred correctly, your new balance is ${}".format(self.balance))
    
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited ${}, your new balance is ${}".format(amount, self.balance))
    
    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn ${}, your new balance is ${}".format(amount, self.balance))

account1 = Account("Luis", 10000, "001")

class ATM(Bank):
    def __init__(self, location, bank_name):
        self.location = location
        self.bank_name = bank_name
        self.balance = 0
    
    def bank_name(self):
        return super().bank_name()
    
    def transfer(self, amount, account):
        if amount > self.balance:
            print("ATM has insufficient funds")
        else:
            self.balance -= amount
            account.transfer(amount)

ATM1 = ATM("Laureles", "Bancolombia")

class Customer:
    def __init__(self, name, id, age, cardnumber, pin):
        self.name = name
        self.id = id
        self.age = age
        self.cardnumber = cardnumber
        self.pin = pin  # Store the PIN during customer creation
    

    def insertcard(self):
        print("Reading card...")
        entered_pin = input("Please enter your PIN:  ")
        if entered_pin == self.pin:  # Check if entered PIN matches the stored PIN
            option = input("Please enter your option (Transfer/Deposit/Withdraw):  ")
            if option == "Transfer":
                amount = int(input("Please enter the amount to transfer:  "))
                ATM1.transfer(amount, account1)
            elif option == "Deposit":
                amount = int(input("Please enter the amount to deposit:  "))
                account1.deposit(amount)
            elif option == "Withdraw":
                amount = int(input("Please enter the amount to withdraw:  "))
                account1.withdraw(amount)
            else:
                print("Invalid option")
        else:
            print("Invalid PIN")

# Create a customer with a PIN
customer1 = Customer("Daniel", 100, 23, "1", "1234")  # Replace "1234" with the desired PIN
customer1.insertcard()
